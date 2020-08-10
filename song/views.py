from django.shortcuts import render
from django.views.generic import *
from . models import Song


class IndexView(ListView):
    model = Song
    template_name = 'song/song_list.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['navbar_title'] = 'AAC로 노래해요'
        context['navbar_subtitle'] = 'AAC로 노래해요'
        return context


class DetailView(DetailView):
    model = Song
    template_name = 'song/song_detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['navbar_title'] = 'AAC로 노래해요'
        context['navbar_subtitle'] = 'AAC로 노래해요'
        return context
