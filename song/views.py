from django.urls import reverse
from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from django.views.generic import *
from .models import *


class IndexView(ListView):
    model = Song
    template_name = 'song/song_list.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['navbar_title'] = 'AAC로 노래해요'
        context['navbar_subtitle'] = 'AAC 카드를 통해 노래를 배워봅시다.'
        context['navbar_background'] = 'background: linear-gradient(90deg, rgba(255, 113, 134, 1) 0%, rgba(236, 170, 97, 1) 50%, rgba(218, 221, 64, 1) 100%);'
        return context


class DetailView(DetailView):
    model = Song
    template_name = 'song/song_detail.html'

    def get_context_data(self, **kwargs):
        image = Image.objects.select_related('song')
        context = super(DetailView, self).get_context_data(**kwargs)
        context['navbar_title'] = 'AAC로 노래해요'
        context['navbar_subtitle'] = 'AAC 카드를 통해 노래를 배워봅시다.'
        context['navbar_background'] = 'background: linear-gradient(90deg, rgba(255, 113, 134, 1) 0%, rgba(236, 170, 97, 1) 50%, rgba(218, 221, 64, 1) 100%);'
        context['images'] = image
        return context
