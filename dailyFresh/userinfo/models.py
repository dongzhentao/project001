# coding:utf-8
from django.db import models


# 定义用户个人信息类
class UserInfo(models.Model):
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=40)
    uphone = models.CharField(max_length=11)
    umail = models.CharField(max_length=20)


# 收件人模型类
class Ushou(models.Model):
    shouname = models.CharField(max_length=20)
    shouphone = models.CharField(max_length=11)
    shouaddress = models.CharField(max_length=100, default='')
    shoupost = models.CharField(max_length=6, default='')
    shouinfo = models.ForeignKey('UserInfo')
