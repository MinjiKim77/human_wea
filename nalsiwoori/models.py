from django.db import models
from django.utils import timezone
from account.models import User

class Users(models.Model): 
    user_name= models.CharField(max_length=64)
    user_email= models.EmailField(max_length=64)
    user_nick= models.CharField(max_length=64)
    user_pw = models.CharField(max_length=64)

class map_data(models.Model):
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    lat = models.IntegerField(max_length=255)
    lng = models.IntegerField(max_length=255)
    map_x = models.IntegerField(max_length=255)
    map_y = models.IntegerField(max_length=255)

class Selection(models.Model):
    user_data = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    map_data = models.ForeignKey(map_data, on_delete=models.CASCADE, null=True)
    map_idx = models.IntegerField(max_length=255)

    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    cur_wea = models.CharField(max_length=255)
    pub_date = models.DateTimeField(default=timezone.now())