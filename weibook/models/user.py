# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class UserModel(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30,default='用户名',blank=True)
    sex = models.IntegerField(default=0,blank=True)
    phone = models.CharField(max_length=11,blank=False)
    location = models.CharField(max_length=255,blank=True)
    qq = models.CharField(max_length=20,blank=True)
    weiChat = models.CharField(max_length=20,blank=True)
    company = models.CharField(max_length=50,blank=True)