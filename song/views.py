from django.shortcuts import render
from django.views.generic import *
from . models import Song


class IndexView(ListView):
    model = Song
    template_name = 'song/song_list.html'


class DetailView(DetailView):
    model = Song
    template_name = 'song/song_detail.html'
