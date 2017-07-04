# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-04 17:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weibook', '0018_auto_20170704_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='datetime',
        ),
        migrations.AddField(
            model_name='comment',
            name='create_datetime',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='comment',
            name='imgs',
            field=models.ManyToManyField(blank=True, related_name='comment_imgs', to='weibook.Image'),
        ),
    ]