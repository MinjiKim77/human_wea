from django.db import models

class User(models.Model):
    nick = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    user_id = models.CharField(max_length=255)
    user_pw = models.CharField(max_length=255)