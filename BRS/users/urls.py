from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('login_user', views.login_user, name='login_user'),
    path('success', views.success, name='success'),
    path('logout_user', views.logout_user, name='logout_user'),
]