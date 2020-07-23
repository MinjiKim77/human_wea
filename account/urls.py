from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'account'
urlpatterns = [
    # path('home/', views.home, name='home'),
    path('', views.login, name='login'),
    path('login_function/', views.login_function, name = 'login_function'),
    path('signup/', views.signup, name='signup'), 
    path('signup_function/', views.signup_function, name = 'login_function'),
    path('find_id/', views.find_id, name='find_id'), 
    path('find_id_function/', views.find_id_function, name='find_id_function'), 
    path('find_pw/', views.find_pw, name='find_pw'), 
    path('find_pw_function/', views.find_pw_function, name='find_pw_function'), 
    path('logout/', views.logout, name='logout'),        
            
]