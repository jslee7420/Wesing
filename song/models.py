from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=250)
    audio = models.FileField(default='')
    lyric = models.TextField()
    like = models.PositiveIntegerField(default=0)
    view = models.PositiveIntegerField(default=0)
