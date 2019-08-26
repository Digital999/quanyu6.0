from django.contrib import admin
from .models import userinfo
admin.site.site_title='全域旅游后台管理系统'
admin.site.site_header='全域旅游后台管理系统'
@admin.register(userinfo)                                          #第一步，需要把这个app下，需要管理的模型注册到admin后台当中，继承的是admin.ModelAdmin
class ProductAdmin(admin.ModelAdmin):                              #接下来的设置是进入模型之后界面的设置
    #进入app后展示的自定义展示的模型信息
    list_display = ['username','location','is_starff']
    #进入app后增加的搜索框的可搜索内容,如果有外键,使用双下划綫,连接两个字段.
    search_fields = ['username','location']
    #设置数据展示界面的排序方式
    ordering = ['username']
    #设置只读字段,在整个admin设置只读的字段
    readonly_fields = ['is_starff']
    #设置过滤器,在页面右侧生成过滤字段
    list_filter = ['location']
    #设置添加数据时的可添加字段
    # fields = ['']