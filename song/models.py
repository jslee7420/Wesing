from django.db import models
from django.conf import settings
from accounts.models import User


class Song(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    audio = models.FileField(upload_to='aac/')
    lyric = models.TextField()
    timeline = models.TextField()
    like = models.ManyToManyField(User)
    view = models.PositiveIntegerField(default=0)


def get_image_filename(instance, filename):
    id = instance.post.id
    return "aac/%s" % (id)


class Images(models.Model):
    song = models.ForeignKey(
        Song, blank=False, null=False, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_image_filename,
                              verbose_name='Image')
