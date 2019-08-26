from django.apps import AppConfig
import os
default_app_config='user.UserConfig'
def get_current_app_name(_file):
    return os.path.split(os.path.dirname(_file))[-1]
class UserConfig(AppConfig):
    name=get_current_app_name(__file__)
    verbose_name='用户'
"""
以上代码的作用是为了在更改相应app在admin后台的显示,
首先获取当前默认情况下app的整个类,
再通过get_current_app_name函数截取获取app的名字,
最后通过重写定义名字的类,来更改用户名
"""