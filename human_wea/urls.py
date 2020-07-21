from django.contrib import admin
from django.urls import path
from nalsiwoori import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('login/', views.login, name='login'),    
    path('logout/', views.logout, name='logout'),        
    path('course/', views.course, name='course'),        
    path('log_wea/', views.log_wea, name='log_wea'),        
]
