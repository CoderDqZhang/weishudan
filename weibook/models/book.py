# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from weibook.models import user

class Book(models.Model):
    id = models.AutoField(primary_key=True,blank=False)
    sbncode = models.CharField(max_length=255,blank=False)
    tags = models.ManyToManyField('Tags',related_name='tags')
    comments = models.ManyToManyField('Comment',related_name='comments')
    uid = models.ForeignKey(user.UserModel,on_delete=models.CASCADE, related_name = 'user_add_book')


class Comment(models.Model):
    id = models.AutoField(primary_key=True,blank=False)
    text = models.CharField(max_length=255,blank=True)
    imgs = models.ManyToManyField('Image',related_name="comment_imgs", blank=True)
    create_datetime = models.DateTimeField(default=datetime.now)
    uid = models.ForeignKey(user.UserModel,on_delete=models.CASCADE, related_name = 'comment_user', blank=False)


class Image(models.Model):
    id = models.AutoField(primary_key=True,blank=False)
    url = models.CharField(max_length=255,blank=False)

class Tags(models.Model):
    id = models.AutoField(primary_key=True,blank=False)
    tag_str = models.CharField(max_length=255)