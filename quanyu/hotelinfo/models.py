from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class hotel(models.Model):
    id = models.AutoField('序号',primary_key=True)
    name = models.CharField('酒店名',max_length=50,null=True,blank=True)
    nowman = models.CharField('入住率',max_length=3,null=True,blank=True)
    def __str__(self):
        return self.name
class hotelinfo(models.Model):
    id = models.AutoField('序号', primary_key=True)
    hotel_name = models.CharField('酒店名', max_length=200, null=True, blank=True)
    location = models.CharField('酒店位置',max_length=200,null=True)
    pinfen = models.CharField('评分', max_length=50)
    customer = models.CharField('消费水平', max_length=50, null=True, blank=True)
    price = models.CharField('均价', max_length=10)
    images = models.CharField('酒店图片', max_length=200)
    city = models.CharField('城市名', max_length=50)
    left_home=models.IntegerField('剩余房间数量',null=True,blank=True,default='0')
    def __str__(self):
        return self.hotel_name
    class Meta:
        verbose_name='酒店信息'
        verbose_name_plural='酒店信息'

