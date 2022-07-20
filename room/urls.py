from unicodedata import name
from django.urls import path
from . import views
import room

urlpatterns = [
    path('', views.rooms, name='rooms'),
    path('<slug:slug>/', views.room, name='room'),
]
