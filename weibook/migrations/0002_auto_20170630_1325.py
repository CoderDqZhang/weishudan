# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 13:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weibook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='sex',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='username',
            field=models.CharField(default='\u8fd8\u6ca1\u8bbe\u7f6e\u7528\u6237\u540d', max_length=30),
        ),
    ]
