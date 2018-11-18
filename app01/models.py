from django.db import models

# Create your models here.


class HostList(models.Model):
    id = models.AutoField(primary_key=True)
    hostname = models.CharField(max_length=64, blank=True, null=True, verbose_name="主机名")
    ip_address = models.CharField(max_length=32, blank=True, null=True, verbose_name="IP地址")
    application = models.CharField(max_length=64, verbose_name="应用")
    version = models.CharField(max_length=32, verbose_name="服务器型号")
    config = models.CharField(max_length=64, verbose_name="服务器配置")
    location_choices = (
        (0, "世纪互联"),
        (1, "光环新网"),
        (2, "亦庄机房"),
        (3, "阿里云"),
        (4, "CDN机房"),
        (5, "公司内网"),
                        )
    location = models.IntegerField(choices=location_choices, verbose_name="存放地点")
    deadline = models.DateField(max_length=32, verbose_name="过期时间")

    def __str__(self):
        return "%s %s %s" %(self.hostname, self.ipaddr, self.deadline)


class User(models.Model):
    username = models.CharField(primary_key=True, max_length=32, verbose_name="用户名")
    password = models.CharField(max_length=32, verbose_name="密码")

