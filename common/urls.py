from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'common'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup1/', views.signup1, name='signup1'),
    path('signup2/', views.signup2, name='signup2'),
    path('signup3/', views.signup3, name='signup3'),
    path('find_id/', views.find_id, name='find_id'),
    path('find_password/', views.find_password, name='find_password'),    
]
