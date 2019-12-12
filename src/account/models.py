from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_certified = models.BooleanField(default=False)
    level_completed = models.PositiveSmallIntegerField(default=0)

    def clean(self):
        super().clean()
        self.username = self.email
