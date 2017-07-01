# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 18:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weibook', '0005_auto_20170630_1853'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='company',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usermodel',
            name='location',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usermodel',
            name='phone',
            field=models.CharField(default=1, max_length=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usermodel',
            name='qq',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usermodel',
            name='sex',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='username',
            field=models.CharField(default='\u8fd8\u6ca1\u8bbe\u7f6e\u7528\u6237\u540d', max_length=30),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='weiChat',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
