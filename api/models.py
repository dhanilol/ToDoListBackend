from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=32)
    desc = models.CharField(max_length=256)
    done = models.BooleanField()
