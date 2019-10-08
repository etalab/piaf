from django.db import models
from django.contrib.auth.models import User

STATUSES = [
    ("pending", "pending"),
    ("progress", "progress"),
    ("completed", "completed"),
]


class Article(models.Model):
    name = models.CharField(max_length=100)


class ParagraphBatch(models.Model):
    user = models.ForeignKey(User, null=True, on_delete="null")
    participated_at = models.DateField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUSES, default="pending")

    @property
    def article(self):
        return Paragraph.objects.filter(batch=self).first().article


class Paragraph(models.Model):
    article = models.ForeignKey(Article, on_delete="cascade", related_name="paragraphs")
    batch = models.ForeignKey(
        ParagraphBatch, on_delete="cascade", related_name="paragraphs"
    )
    text = models.TextField()
    status = models.CharField(max_length=10, choices=STATUSES, default="pending")


class Question(models.Model):
    paragraph = models.ForeignKey(
        Paragraph, on_delete="cascade", related_name="questions"
    )
    text = models.CharField(max_length=200)
    created_at = models.DateField(auto_now_add=True)


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete="null", related_name="answers")
    question = models.ForeignKey(Question, on_delete="cascade", related_name="answers")
    text = models.CharField(max_length=200)
    start_position = models.IntegerField()
    end_position = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
