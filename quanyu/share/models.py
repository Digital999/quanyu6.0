from django.db import models
import django.utils.timezone as timezone
class submmit(models.Model):
    article_id=models.AutoField(primary_key=True)
    title = models.CharField('标题', max_length=50)
    content=models.TextField('内容')
    photo=models.TextField('图片base64',null=True,blank=True)
    author_id=models.CharField(max_length=50)
    author_name=models.CharField(max_length=50,null=True)
    time=models.DateTimeField('提交时间',null=True,blank=True,default=timezone.now)
    touxiang=models.CharField('头像地址',max_length=500)
    gooded=models.IntegerField('被点赞数',default=0,null=True)
    is_pass=models.CharField('是否审核通过',default=0,max_length=1)
    waitselect=models.CharField('是否审核过',default=0,max_length=1)
    city=models.CharField('城市名',null=True,blank=True,max_length=50)
    requests_math=models.IntegerField('访问量',null=True,default=0)
    def __str__(self):
        return self.title
class good(models.Model):
    id=models.AutoField(primary_key=True)
    author_id=models.CharField('用户标志',max_length=50)
    article_id=models.CharField('文章标识',max_length=50)
    is_good=models.CharField('是否点赞标志',max_length=1,default=0)
    is_keep=models.CharField('是否收藏的标志',max_length=1,default=0)


class PicTest(models.Model):
    goods_pic = models.ImageField(upload_to='booktest/')