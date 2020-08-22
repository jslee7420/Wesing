from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('board/', include('board.urls')),
    path('song/', include('song.urls')),
    path('common/', include('common.urls')),
    path('',views.index, name='index'),
]
