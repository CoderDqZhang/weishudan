# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from weibook.models import user

class Book(models.Model):
    id = models.AutoField(primary_key=True,blank=False)
    sbncode = models.CharField(max_length=255,blank=False)
    tags = models.CharField(max_length=255,blank=False)
    uid = models.ForeignKey(user.UserModel,on_delete=models.CASCADE, related_name = 'user_add_book')
