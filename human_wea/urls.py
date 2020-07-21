from django.contrib import admin
from django.urls import path
from nalsiwoori import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
<<<<<<< HEAD
    path('signup/', views.signup, name='signup'), 
    path('login/', views.login, name='login'),   
=======
    # path('login/', views.login, name='login'),    
>>>>>>> c50ccb78f04b5be7801aa553f760ab2802dbfed8
    path('logout/', views.logout, name='logout'),        
    path('course/', views.course, name='course'),        
    path('log_wea/', views.log_wea, name='log_wea'),        
]
