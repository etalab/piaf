from django.test import Client, TestCase
from django.contrib.auth import get_user_model

from .models import Article, Paragraph, ParagraphBatch, Question, Answer

client = Client()


questions_answers = [
    {"question": {"text": "q1"}, "answer": {"text": "a1", "index": 11}},
    {"question": {"text": "q2"}, "answer": {"text": "a2", "index": 12}},
    {"question": {"text": "q3"}, "answer": {"text": "a3", "index": 13}},
    {"question": {"text": "q4"}, "answer": {"text": "a4", "index": 14}},
    {"question": {"text": "q5"}, "answer": {"text": "a5", "index": 15}},
]


def create_article(name, theme, text, audience="all"):
    article = Article.objects.create(name=name, theme=theme, audience=audience)
    batch = ParagraphBatch.objects.create()
    Paragraph.objects.create(text=text, article=article, batch=batch)
    return article


def create_question(paragraph, text):
    return Question.objects.create(paragraph=paragraph, text=text)


class ModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(username="user")
        self.article = Article.objects.create(
            name="My First Article", theme="Géographie"
        )
        self.batch = ParagraphBatch.objects.create()
        self.paragraphs = [
            Paragraph.objects.create(
                text=f"this is text {i}", article=self.article, batch=self.batch
            )
            for i in range(2, 5)
        ]

    def test_update_paragraph_also_updates_batch_status(self):
        self.assertEqual(self.batch.status, "pending")
        self.paragraphs[0].complete(questions_answers, user=self.user)
        self.assertEqual(self.batch.status, "progress")
        for p in self.paragraphs:
            if p.status == "pending":
                p.complete(questions_answers, user=self.user)
        self.assertEqual(self.batch.status, "completed")

    def test_3_answers_complete_question(self):
        article = create_article("article", "g", "text")
        question = Question.objects.create(paragraph=article.paragraphs.first(), text="q")
        Answer.objects.create(question=question, text="a1", index=1)
        Answer.objects.create(question=question, text="a2", index=2)
        self.assertEqual(question.status, "pending")
        answer = Answer(question=question, text="a3", index=3)
        answer.save()
        self.assertEqual(question.status, "completed")



def login_user():
    user = get_user_model().objects.create(username="user")
    user.set_password("password")
    user.save()
    client.login(username="user", password="password")
    return user


class ParagraphApiTest(TestCase):
    def setUp(self):
        # create user and authenticate
        self.user = login_user()
        # 1 article with 1 batch and 5 articles
        self.article = create_article(
            name="My First Article", theme="Géographie", text="this is text 1"
        )
        for i in range(2, 5):
            Paragraph.objects.create(
                text=f"this is text {i}",
                article=self.article,
                batch=self.article.batches[0],
            )
        self.paragraphs = self.article.paragraphs

    def test_me_values(self):
        response = client.get("/app/me")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["is_certified"], False)
        self.assertEqual(response.json()["paragraphs_count"], 0)

    def test_get_paragraph(self):
        response = client.get("/app/api/paragraph")
        self.assertEqual(response.status_code, 200)
        self.assertDictContainsSubset(
            {
                "theme": "Géographie",
                "text": "this is text 1",
                "title": "My First Article",
                "count_pending_paragraphs": 4,
                "count_pending_batches": 1,
            },
            response.json(),
        )

    def test_post_paragraph(self):
        client.post(
            "/app/api/paragraph",
            content_type="application/json",
            data={"paragraph": self.paragraphs.first().pk, "data": questions_answers},
        )

        paragraph = Article.objects.first().paragraphs.first()
        sample_question = paragraph.questions.all()[2]
        sample_answer = sample_question.answers.first()
        self.assertEqual(paragraph.questions.count(), 5)
        self.assertEqual(sample_question.text, "q3")
        self.assertEqual(sample_answer.text, "a3")
        self.assertEqual(paragraph.status, "completed")
        self.assertEqual(paragraph.user.username, "user")
        self.assertEqual(sample_answer.user.username, "user")

    def test_get_paragraph_theme(self):
        for i in range(0, 100):
            create_article(name=f"article {i}", theme="notmychoice", text=f"text {i}")
        create_article(name=f"article I like", theme="mychoice", text=f"text I like")
        create_article(
            name=f"other article I like", theme="mychoice", text=f"text I like"
        )

        response = client.get("/app/api/paragraph?theme=mychoice")
        self.assertEqual(response.json().get("theme"), "mychoice")

    def test_get_paragraph_pending_only(self):
        response = client.get("/app/api/paragraph")
        self.assertEqual(response.json()["text"], "this is text 1")
        Paragraph.objects.filter(pk__lte=int(response.json()["id"]) + 2).update(
            status="complete"
        )
        response = client.get("/app/api/paragraph")
        self.assertEqual(response.json()["text"], "this is text 4")

    def test_get_paragraph_limits_restricted_articles_to_certified_users(self):
        Article.objects.filter(pk=self.article.pk).update(audience="restricted")
        response = client.get("/app/api/paragraph")
        self.assertEqual(response.json(), {})
        get_user_model().objects.filter(pk=self.user.pk).update(is_certified=True)
        response = client.get("/app/api/paragraph")
        self.assertEqual(response.json()["text"], "this is text 1")

    def test_paragraph_are_suggested_in_order_for_a_user(self):
        for i in range(0, 100):
            create_article(
                name=f"rand article {i}", theme="default", text=f"rand text {i}"
            )
        response = client.get("/app/api/paragraph")
        self.assertNotEqual(response.json()["text"], "this is text 1")
        self.paragraphs.first().complete(questions_answers, user=self.user)
        response = client.get("/app/api/paragraph")
        self.assertEqual(response.json()["text"], "this is text 2")

    def test_get_datasets_info(self):
        response = client.get("/app/api/datasets")
        self.assertEqual(response.status_code, 200)
        # import ipdb; ipdb.set_trace()
        self.assertDictEqual(
            response.json(),
            {"count_pending_articles": 1, "count_completed_articles": 0},
        )
        paragraph = self.paragraphs.first()
        paragraph.status = "completed"
        paragraph.save()
        response = client.get("/app/api/datasets")
        self.assertDictEqual(
            response.json(),
            {"count_pending_articles": 1, "count_completed_articles": 0},
        )
        for p in self.paragraphs.all():
            p.status = "completed"
            p.save()
        response = client.get("/app/api/datasets")
        self.assertDictEqual(
            response.json(),
            {"count_pending_articles": 0, "count_completed_articles": 1},
        )


class QuestionApiTest(TestCase):
    def setUp(self):
        self.user = login_user()

    def test_question_is_accessible(self):
        response = client.get("/app/api/question")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {})

    def test_question_returns_json_dict(self):
        article = create_article("title 1", "general", "this is article 1")
        question = Question.objects.create(
            paragraph=article.paragraphs.first(), text="What is it?"
        )
        response = client.get("/app/api/question")
        self.assertDictEqual(
            response.json(),
            {
                "id": question.id,
                "text": "What is it?",
                "paragraph": {
                    "id": question.paragraph.id,
                    "theme": "general",
                    "title": "title 1",
                    "text": "this is article 1",
                },
            },
        )

    def test_post_answer_to_question(self):
        article = create_article("title 1", "general", "this is article 1")
        question = Question.objects.create(
            paragraph=article.paragraphs.first(), text="What is it?"
        )
        self.assertEqual(Answer.objects.count(), 0)
        client.post(
            "/app/api/question",
            content_type="application/json",
            data={"id": question.pk, "text": "This is the answer", "index": 42},
        )
        self.assertEqual(Answer.objects.count(), 1)

    def test_get_answer_only_pending_question(self):
        article = create_article("title 1", "general", "this is article 1")
        paragraph = article.paragraphs.first()
        for i in range(0, 20):
            Question.objects.create(paragraph=paragraph, status="completed", text=f"q {i}")
        Question.objects.create(paragraph=paragraph, text="I'm pending")
        response = client.get("/app/api/question")
        self.assertEqual(response.json()["text"], "I'm pending")
