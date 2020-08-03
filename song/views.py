from django.shortcuts import render
from django.views.generic import *
from . models import Song


class SongList(ListView):
    model = Song
