from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('board/', include('board.urls')),
    path('song/', include('song.urls')),
    path('activity/', include('activity.urls')),
    path('common/', include('common.urls')),
]
