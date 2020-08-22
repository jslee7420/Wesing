from django.urls import reverse
from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from django.views.generic import *
from song.models import *


class IndexView(ListView):
    model = Song
    template_name = 'activity/activity_list.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['navbar_title'] = 'AAC로 활동해요'
        context['navbar_subtitle'] = 'AAC 카드로 배운 노래를 응용해서 활동해보아요.'
        context['navbar_background'] = 'background: linear-gradient(90deg, rgba(255,113,134,1) 0%, rgba(255,162,0,1) 0%, rgba(255,118,67,1) 100%);'
        return context


class DetailView(DetailView):
    model = Song
    template_name = 'activity/activity_detail.html'

    def get_context_data(self, **kwargs):
        image = Image.objects.select_related('song')
        context = super(DetailView, self).get_context_data(**kwargs)
        context['navbar_title'] = 'AAC로 활동해요'
        context['navbar_subtitle'] = 'AAC 카드로 배운 노래를 응용해서 활동해보아요.'
        context['navbar_background'] = 'background: linear-gradient(90deg, rgba(255,113,134,1) 0%, rgba(255,162,0,1) 0%, rgba(255,118,67,1) 100%);'
        context['images'] = image
        return context
