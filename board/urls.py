from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('answer/create/<int:post_id>',views.answer_create, name='answer_create'),
    path('post/delete/<int:post_id>/',views.post_delete, name='post_delete'),
]
