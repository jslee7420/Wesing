from django.urls import path
from django.conf.urls import url
from .views import *


app_name = "song"

urlpatterns = [
    path('', IndexView.as_view(), name='song_index'),
    # url('<pk>/', SongList.as_view(), name='song_detail'),
    path('<int:pk>/', DetailView.as_view(), name='song_detail'),
    path('<int:pk>/', DetailView.as_view(), name='song_detail'),
]

# song/
# song/<pk >
