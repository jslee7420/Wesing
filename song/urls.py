from django.urls import path
from django.conf.urls import url
from .views import SongList


app_name = "song"

urlpatterns = [
    url('', SongList.as_view()),
]

# song/
# song/<pk >
