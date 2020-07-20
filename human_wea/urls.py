from django.contrib import admin
from django.urls import path
from nalsiwoori import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),    
    path('logout/', views.logout, name='logout'),        
    path('board/', views.board, name='board'),        
]
