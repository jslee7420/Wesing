from django.urls import path
from django.conf.urls import url
from .views import *


app_name = "activity"

urlpatterns = [
    path('', IndexView.as_view(), name='activity_index'),
    # url('<pk>/', SongList.as_view(), name='song_detail'),
    path('<int:pk>/', DetailView.as_view(), name='activity_detail'),
]
