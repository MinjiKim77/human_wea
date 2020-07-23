from django.contrib import admin
from django.urls import path,include
from nalsiwoori import views
from account import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('account.urls')),
    # path('account/',include('account.urls')),             
    # path('nalsiwoori/',include('nalsiwoori.urls')), 
    path('',include('nalsiwoori.urls')), 
                
]
