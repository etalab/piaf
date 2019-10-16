from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

STATUS_PENDING = "pending"
STATUS_PROGRESS = "progress"
STATUS_COMPLETED = "completed"
STATUSES = [STATUS_PENDING, STATUS_PROGRESS, STATUS_COMPLETED]

THEMES = ["Religion", "Géographie", "Histoire", "Sport", "Art", "Société", "Sciences"]
THEME_SLUGS = [slugify(t) for t in THEMES]
THEME_CHOICES = zip(THEME_SLUGS, THEMES)

AUDIENCES = ["restricted", "all"]
AUDIENCE_CHOICES = zip(AUDIENCES, AUDIENCES)


# Monkeypatch User to add a `is_certified` property without resetting the whole
# Django database subclassing auth.User
setattr(User, "is_certified", lambda u: u.email.endswith(".gouv.fr"))


class Article(models.Model):
    name = models.CharField(max_length=100)
    theme = models.CharField(max_length=20, choices=THEME_CHOICES)
    reference = models.CharField(max_length=10)
    audience = models.CharField(max_length=10, choices=AUDIENCE_CHOICES)

    @property
    def batches(self):
        return ParagraphBatch.objects.filter(paragraphs__article=self)


class ParagraphBatch(models.Model):
    user = models.ForeignKey(User, null=True, on_delete="null")
    participated_at = models.DateField(auto_now=True)
    status = models.CharField(
        max_length=10, choices=zip(STATUSES, STATUSES), default="pending"
    )

    @property
    def article(self):
        return Paragraph.objects.filter(batch=self).first().article


class Paragraph(models.Model):
    article = models.ForeignKey(Article, on_delete="cascade", related_name="paragraphs")
    batch = models.ForeignKey(
        ParagraphBatch, on_delete="cascade", related_name="paragraphs"
    )
    text = models.TextField()
    status = models.CharField(
        max_length=10, choices=zip(STATUSES, STATUSES), default="pending"
    )
    user = models.ForeignKey(User, on_delete="null", null=True)

    def complete(self, questions_answers, user=None):
        if self.status == STATUS_COMPLETED:
            raise Exception("The Paragraph is completed already.")
        if not len(questions_answers) == 5:
            raise Exception(
                "A Paragraph requires 5 questions and answers to be completed."
            )
        for qa in questions_answers:
            question = Question.objects.create(
                text=qa["question"]["text"], paragraph=self
            )
            answer = Answer.objects.create(
                question=question,
                text=qa["answer"]["text"],
                index=qa["answer"]["index"],
                user=user,
            )
        self.status = STATUS_COMPLETED
        self.user = user
        self.save()


class Question(models.Model):
    paragraph = models.ForeignKey(
        Paragraph, on_delete="cascade", related_name="questions"
    )
    text = models.CharField(max_length=200)
    created_at = models.DateField(auto_now_add=True)


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete="null", related_name="answers", null=True)
    question = models.ForeignKey(Question, on_delete="cascade", related_name="answers")
    text = models.CharField(max_length=200)
    index = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
