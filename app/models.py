from operator import mod
from django.db import models


class TodoModel(models.Model):
    title = models.CharField(max_length=256)
    body = models.TextField()
    status = models.BooleanField(default=False)

    