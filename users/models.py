from django.db import models
from datetime import datetime


class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.email
