from django.db import models
from django.utils.html import format_html
# Create your models here.
class userinfo(models.Model):
    id = models.AutoField('序号', primary_key=True)
    username = models.CharField('用户名', max_length=50, null=True, blank=True)
    images = models.CharField('头像地址', max_length=200, null=True, blank=True)
    location = models.CharField('地址', max_length=15, null=True, blank=True)
    openid = models.CharField('用户唯一标识', max_length=50, null=True, blank=True)
    is_starff=models.CharField('是否为管理员',max_length=1,default=0)
    def __str__(self):
        return self.openid
    def colored_type(self):
        if '1' in self.is_starff:
            color_code='red'
        else:
            color_code='blue'
        return format_html(
            '<span style="color:{};">{}</span>',
            color_code,
            self.username
        )
    class Meta:
        verbose_name='用户信息'
        verbose_name_plural='用户信息'
