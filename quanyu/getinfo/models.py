from django.db import models
from django.contrib.auth.models import AbstractUser
import django.utils.timezone as timezone
# Create your models here.
class EveryComponent(models.Model):
    id=models.AutoField('每一条评论的主键',primary_key=True)
    hotel_name=models.CharField('酒店名',max_length=50)
    openid=models.CharField('用户唯一标识',max_length=50)
    time=models.DateTimeField('评论时间',auto_now_add=True)
    username=models.CharField('用户昵称',max_length=50)
    touxiang=models.CharField('用户头像',max_length=200)
    content=models.CharField('评论内容',max_length=200,null=True)
    comment_amount=models.IntegerField('评论数',null=True,blank=True,default=0)
    target=models.CharField('上级评论的序号',max_length=50,default='0')
class Xiuxianyule(models.Model):
    id=models.AutoField('序号',primary_key=True)
    name=models.CharField('店名',max_length=50)
    star=models.CharField('星级',max_length=10)
    pinfen=models.CharField('评分',max_length=10)
    customer=models.CharField('人均消费',max_length=10)
    location=models.CharField('地址',max_length=50)
    phone=models.CharField('电话',max_length=50)
    open_time=models.CharField('营业时间',max_length=50)
    image=models.CharField('图片',max_length=500)
    type=models.CharField('类型',max_length=10,null=True)
    city=models.CharField('城市名',max_length=50,null=True)
    def __str__(self):
        return self.name
class Xiuxiannongjia(models.Model):
    id=models.AutoField('序号',primary_key=True)
    name=models.CharField('店名',max_length=50)
    pinfen=models.CharField('评分',max_length=50)
    comment_amount=models.CharField('评分人数',max_length=50)
    images=models.CharField('图片',max_length=500,null=True)
    location=models.CharField('位置',max_length=50)
    price=models.CharField('价格',max_length=50)
    city=models.CharField('城市',max_length=50,null=True)
    def __str__(self):
        return self.name
