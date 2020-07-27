from django.contrib import admin
from django.urls import path
from .import views

app_name = 'nalsiwoori'
urlpatterns = [
    path('load_map_db/', views.load_map_db, name='load_map_db'),
    path('home/', views.home, name='home'),
    path('weather/', views.weather, name='weather'),
    path('log_wea/', views.log_wea, name='log_wea'),
    path('load_sel_db/', views.load_sel_db, name='load_sel_db'),
]  