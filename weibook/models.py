# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class UserModel(models.Model):
    id = models.CharField(max_length=255,primary_key=True)
    username = models.CharField(max_length=30,default='还没设置用户名')
    sex = models.IntegerField(default=0)
    phone = models.CharField(max_length=11)
    location = models.CharField(max_length=255)
    qq = models.CharField(max_length=20)
    weiChat = models.CharField(max_length=20)
    company = models.CharField(max_length=50)
    # def __init__(self, **kwargs):
    #     super(UserModel, self).__init__(**kwargs)