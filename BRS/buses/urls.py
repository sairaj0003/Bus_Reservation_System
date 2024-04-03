from django.urls import path

from . import views

urlpatterns = [
    path('findbus', views.findBus, name='findbus'),
    path('list', views.list, name='list'),
    path('booklist', views.booklist, name='booklist'),
    path('booking', views.booking, name='booking'),
    path('cancel', views.cancel, name='cancel'),
]