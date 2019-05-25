from django.db import models
from django.contrib.auth.models import User


class MelkUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_blocked = models.BooleanField(default=False)
