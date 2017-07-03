# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-01 06:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('weibook', '0007_delete_usermodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.IntegerField(db_column='FId', primary_key=True, serialize=False)),
                ('username', models.CharField(default='\u8fd8\u6ca1\u8bbe\u7f6e\u7528\u6237\u540d', max_length=30)),
                ('sex', models.IntegerField(default=0)),
                ('phone', models.CharField(max_length=11)),
                ('location', models.CharField(max_length=255)),
                ('qq', models.CharField(max_length=20)),
                ('weiChat', models.CharField(max_length=20)),
                ('company', models.CharField(max_length=50)),
            ],
        ),
    ]