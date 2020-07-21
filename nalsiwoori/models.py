from django.db import models

class Selection(models.Model):
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    cur_wea = models.CharField(max_length=255)
    # pub_date = models.DateTimeField('date published')
    # def __str__(self):
    #     return '지금 %s %s %s의 날씨는 %s입니다 !!!' % (self.state, self.city, self.street, self.cur_wea)

class Users(models.Model): #장고에서 제공하는 models.Model를 상속받아야한다.
    user_name= models.CharField(max_length=64)
    user_email= models.EmailField(max_length=64)
    user_nick= models.CharField(max_length=64)
    user_pw = models.CharField(max_length=64)