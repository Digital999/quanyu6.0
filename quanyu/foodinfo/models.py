from django.db import models

# Create your models here.
class food(models.Model):
    id = models.AutoField('序号',primary_key=True)
    imgpath = models.CharField('食物照片',max_length=200,null=True,blank=True)
    title = models.CharField('店家名',max_length=50)
    star = models.CharField('星级',max_length=50,null=True,blank=True)
    price = models.CharField('价格',max_length=10)
    distance = models.CharField('距离',max_length=50)
    labels =models.CharField('标签',max_length=50)
    evaluate = models.CharField('奖项',max_length=50)
    group = models.CharField('组队优惠信息',max_length=50)
    coupons = models.CharField('优惠券信息',max_length=50)
    def __str__(self):
        return self.title