from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_certified = models.BooleanField(default=False)
    level_completed = models.PositiveSmallIntegerField(default=0)

    @property
    def answers_count(self):
        return self.answers.count()

    @property
    def additional_answers_count(self):
        return self.answers.count() - (self.paragraphs.count() * 5)

    @property
    def paragraphs_count(self):
        return self.paragraphs.count()

    def clean(self):
        super().clean()
        self.username = self.email
