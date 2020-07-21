from django.contrib.auth.models import User
from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=250)
    audio = models.FileField(upload_to='timeline_photo/%Y/%m/%d')
    lyric = models.TextField()
    like = models.ManyToManyField(User)
    view = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
