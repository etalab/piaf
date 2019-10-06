from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    CHOICES = [('pending', 'pending'), ('progress', 'progress'), ('completed', 'completed')]
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=CHOICES, default='pending')
    user = models.ForeignKey(User, null=True, on_delete='null')
    participated_at = models.DateField(auto_now=True)


class Paragraph(models.Model):
    article = models.ForeignKey(Article, on_delete='cascade', related_name='paragraphs')
    text = models.TextField()


class Question(models.Model):
    paragraph = models.ForeignKey(Paragraph, on_delete='cascade', related_name='questions')
    text = models.CharField(max_length=200)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete='cascade', related_name='answers')
    text = models.CharField(max_length=200)
    start_position = models.IntegerField()
    end_position = models.IntegerField()
