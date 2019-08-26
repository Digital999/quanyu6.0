from django.db import models

# Create your models here.
class customer_team(models.Model):
    id = models.AutoField('序号', primary_key=True)
    name = models.CharField('目标城市', max_length=50, blank=True)
    value = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=10, blank=True)
    def __str__(self):
        return self.name
class customer_age(models.Model):
    id = models.AutoField('序号', primary_key=True)
    name = models.CharField('目标城市', max_length=50, blank=True)
    value = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.name
class customer_tools(models.Model):
    id = models.AutoField('序号', primary_key=True)
    name = models.CharField('目标城市', max_length=50, blank=True)
    value = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.name
class customer_staytime(models.Model):
    id = models.AutoField('序号', primary_key=True)
    name = models.CharField('目标城市', max_length=50, blank=True)
    value_1 = models.CharField(max_length=50, blank=True)
    value_2=models.CharField(max_length=50,blank=True)
    location = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.name

class customer_method(models.Model):
    id = models.AutoField('序号', primary_key=True)
    name = models.CharField('目标城市', max_length=50, blank=True)
    value = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.name

class customer_from(models.Model):
    id = models.AutoField('序号', primary_key=True)
    name = models.CharField('目标城市', max_length=50,blank=True)
    value=models.CharField(max_length=50,blank=True)
    location=models.CharField(max_length=10,blank=True)
    def __str__(self):
        return self.name



    # beijing=models.CharField('北京',max_length=10, null=True, blank=True)
    # shanghai = models.CharField('上海', max_length=10, null=True, blank=True)
    # shenzhen = models.CharField('深圳', max_length=10, null=True, blank=True)
    # guangzhou = models.CharField('广州', max_length=10, null=True, blank=True)
    # hangzhou = models.CharField('杭州', max_length=10, null=True, blank=True)
    # tianjing = models.CharField('天津', max_length=10, null=True, blank=True)
    # chengdu = models.CharField('成都', max_length=10, null=True, blank=True)
    # haerbing = models.CharField('哈尔冰', max_length=10, null=True, blank=True)
    # city = models.CharField('城市名',max_length=15,null=True)

# class city(models.Model):
#     id =models.IntegerField('城市编号',primary_key=True)
#     city_name=models.CharField('城市名',max_length=50)

