from django.test import Client, TestCase

from django.contrib.auth.models import User
from .models import Article, Paragraph, ParagraphBatch

client = Client()


class ApiTest(TestCase):
    def setUp(self):
        user = User.objects.create(username="user")
        user.set_password("password")
        user.save()
        self.user = client.login(username="user", password="password")
        self.article = Article.objects.create(name="My First Article")
        self.batch = ParagraphBatch.objects.create()
        self.paragraphs = []
        for i in range(0, 5):
            paragraph = Paragraph.objects.create(
                text=f"this is text {i + 1}", article=self.article, batch=self.batch
            )
            self.paragraphs.append(paragraph)

    def test_post_annotation(self):
        client.post(
            "/app/api/paragraph",
            content_type="application/json",
            data={
                "paragraph": self.paragraphs[0].pk,
                "data": [
                    {"question": {"text": "q1"}, "answer": {"text": "a1", "index": 11}},
                    {"question": {"text": "q2"}, "answer": {"text": "a2", "index": 12}},
                    {"question": {"text": "q3"}, "answer": {"text": "a3", "index": 13}},
                    {"question": {"text": "q4"}, "answer": {"text": "a4", "index": 14}},
                    {"question": {"text": "q5"}, "answer": {"text": "a5", "index": 15}},
                ],
            },
        )

        paragraph = Article.objects.first().paragraphs.first()
        self.assertEqual(paragraph.questions.count(), 5)
        self.assertEqual(paragraph.questions.last().answers.first().text, "a5")
        self.assertEqual(paragraph.status, "completed")
