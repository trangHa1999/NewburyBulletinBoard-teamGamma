from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(default=0)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    activationKey = models.CharField(blank=True, default="", max_length=64)
    activationExpires = models.DateTimeField(blank=True)