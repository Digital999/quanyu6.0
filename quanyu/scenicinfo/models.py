from django.db import models

# Create your models here.
class scenic(models.Model):
    id = models.AutoField('序号', primary_key=True)
    imgpath = models.CharField('食物照片', max_length=200, null=True, blank=True)
    title = models.CharField('景点名',max_length=200,null=True)
    star = models.CharField('星级',max_length=50,null=True)
    commet = models.CharField('评分', max_length=50)
    location = models.CharField('距离', max_length=50, null=True, blank=True)
    labels = models.CharField('标签', max_length=50)
    prices = models.CharField('价格', max_length=50)
    merit = models.CharField('优惠券', max_length=50)
    visit_pro = models.CharField('亮点', max_length=50)
    def __str__(self):
        return self.title
