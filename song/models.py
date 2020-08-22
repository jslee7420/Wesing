from django.db import models
from django.conf import settings
from accounts.models import User


class Song(models.Model):
    title = models.CharField(max_length=250)
    thumbnail = models.ImageField(upload_to='static/song/thumbnail')
    audio = models.FileField(upload_to='static/song/audio')
    lyric = models.TextField()
    timeline = models.TextField()
    photos = models.TextField()
    like = models.ManyToManyField(User, blank=True)
    view = models.PositiveIntegerField(default=0)


class Image(models.Model):
    song = models.ForeignKey(
        Song, blank=False, null=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='static/song/images')
