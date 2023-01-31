"""site content urls"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_index, name='index'),
]
