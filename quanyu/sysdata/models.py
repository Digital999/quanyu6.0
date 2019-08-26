from django.db import models
# Create your models here.
class admin_role(models.Model):
    id = models.AutoField('编号',primary_key=True)
    name=models.CharField('用户名称',max_length=20)
    password=models.CharField('用户密码',max_length=20)
    role=models.IntegerField('角色编号')
    Role_name=models.CharField('角色名称',max_length=20)
    def __str__(self):
        return self.name
class device(models.Model):
    id = models.AutoField('编号',primary_key=True)
    deviceName=models.CharField('设备名称',max_length=10)
    deviceType=models.CharField('设备类型',max_length=10)
    deviceLng=models.CharField('经度',max_length=10)
    deviceLat=models.CharField('维度',max_length=10)
    deviceNum=models.CharField('设备编号',max_length=10)
    deviceMac=models.CharField('Mac地址',max_length=10)
    deviceArea=models.CharField('才几点放置区域',max_length=10)
    def __str__(self):
        return self.deviceName
class sensor(models.Model):
    id = models.AutoField('编号',primary_key=True)
    mac=models.CharField('采集点Mac地址',max_length=50)
    sensortype=models.CharField('传感器类型',max_length=50)
    value=models.IntegerField('采集值')
    deviceLng = models.CharField('经度', max_length=50)
    deviceLat = models.CharField('维度', max_length=50)
    month=models.CharField('采集时所属月',max_length=50)
    day = models.CharField('采集时所属日', max_length=50)
    hour = models.CharField('采集时所属时', max_length=50)
    fulltime=models.DateTimeField('完成采集时间')
    def __str__(self):
        return self.mac
class sysconfig(models.Model):
    id=models.AutoField('编号',primary_key=True)
    THITIME=models.IntegerField('刷新时间间隔')
    TALARM = models.IntegerField('温度预警阈值')
    TAUTO = models.IntegerField('温度报警是否开启')
    HALARM = models.IntegerField('湿度预警阈值')
    HAUTO = models.IntegerField('湿度报警是否开启')
    IALARM = models.IntegerField('光照预警阈值')
    IAUTO = models.IntegerField('光照报警是否开启')
    CO2ALARM = models.IntegerField('co2预警阈值')
    CO2AUTO = models.IntegerField('co2报警是否开启')
    pm25densityalarm = models.IntegerField('PM2.5预警阈值')
    pm25densityauto = models.IntegerField('PM2.5是否开启')
    pm25particlealarm = models.IntegerField('PM2.5颗粒数预警阈值')
    pm25particleauto = models.IntegerField('PM2.5颗粒数是否开启')
    pm10densityalarm = models.IntegerField('PM10预警阈值')
    pm10particleauto = models.IntegerField('PM10颗粒数是否开启')
    soilphalarm = models.IntegerField('土壤酸碱度最大值')
    soilphmin = models.IntegerField('土壤酸碱度最小值')
    soilphauto = models.IntegerField('土壤酸碱阀值是否开启')


