from django.db import models
from django.conf import settings


class Song(models.Model):
    author = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    audio = models.FileField(upload_to='aac/')
    lyric = models.TextField()
    timeline = models.TextField()
    like = models.ManyToManyField(settings.AUTH_USER_MODEL)
    view = models.PositiveIntegerField(default=0)
