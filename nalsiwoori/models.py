from django.db import models
from django.utils import timezone

class Selection(models.Model):
    state = models.CharField(max_length=255)  # 시도
    city = models.CharField(max_length=255)  # 군구
    street = models.CharField(max_length=255)  # 동읍면리
    cur_wea = models.CharField(max_length=255)  # 현재 날씨
    pub_date = models.DateTimeField(default=timezone.now())
    # def __str__(self):
    #     return '지금 %s %s %s의 날씨는 %s입니다 !!!' % (self.state, self.city, self.street, self.cur_wea)