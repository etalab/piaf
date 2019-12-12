from django.conf import settings
from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model

STATUS_PENDING = "pending"
STATUS_PROGRESS = "progress"
STATUS_COMPLETED = "completed"
STATUSES = [STATUS_PENDING, STATUS_PROGRESS, STATUS_COMPLETED]

THEMES = ["Religion", "Géographie", "Histoire", "Sport", "Arts", "Société", "Sciences"]
THEME_CHOICES = zip(THEMES, THEMES)

AUDIENCES = ["restricted", "all"]
AUDIENCE_CHOICES = zip(AUDIENCES, AUDIENCES)


class Article(models.Model):
    name = models.CharField(max_length=200)
    theme = models.CharField(max_length=20, choices=THEME_CHOICES)
    reference = models.CharField(max_length=10)
    audience = models.CharField(max_length=10, choices=AUDIENCE_CHOICES, default="all")

    @property
    def batches(self):
        return ParagraphBatch.objects.filter(paragraphs__article=self).distinct(
            "paragraphs__article"
        )

    def __str__(self):
        return self.name


class ParagraphBatch(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete="null")
    participated_at = models.DateField(auto_now=True)
    status = models.CharField(
        max_length=10, choices=zip(STATUSES, STATUSES), default="pending"
    )

    @property
    def article(self):
        return Paragraph.objects.filter(batch=self).first().article

    def __str__(self):
        return f"Batch for {self.paragraphs.first().article}"

    def update_status(self, user):
        if not self.user:
            self.user = user
        self.status = (
            STATUS_PROGRESS
            if self.paragraphs.filter(status="pending").count()
            else STATUS_COMPLETED
        )
        self.save()


class Paragraph(models.Model):
    article = models.ForeignKey(Article, on_delete="cascade", related_name="paragraphs")
    batch = models.ForeignKey(
        ParagraphBatch, on_delete="cascade", related_name="paragraphs"
    )
    text = models.TextField()
    status = models.CharField(
        max_length=10, choices=zip(STATUSES, STATUSES), default="pending"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="paragraphs", on_delete="null", null=True
    )

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
        self.batch.update_status(user=user)

    def __str__(self):
        return f"{self.text[:100]}…"


class Question(models.Model):
    paragraph = models.ForeignKey(
        Paragraph, on_delete="cascade", related_name="questions"
    )
    text = models.CharField(max_length=200)
    created_at = models.DateField(auto_now_add=True)
    status = models.CharField(
        max_length=10, choices=zip(STATUSES, STATUSES), default="pending"
    )

    def watch_status(self):
        if self.answers.count() >= 3:
            self.status = STATUS_COMPLETED
            self.save()


class Answer(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete="null", related_name="answers", null=True
    )
    question = models.ForeignKey(Question, on_delete="cascade", related_name="answers")
    text = models.CharField(max_length=200)
    index = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.question.watch_status()


class UserRelevancy(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete="cascade",
        related_name="relevancies",
        null=False,
    )
    level = models.PositiveSmallIntegerField(null=False)
    score = models.PositiveIntegerField(null=False)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}, level {self.level}, {self.score}%"
