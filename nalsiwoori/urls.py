from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('load_map_db/', views.load_map_db, name='load_map_db'),
]