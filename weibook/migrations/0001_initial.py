# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 12:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('sex', models.IntegerField()),
                ('phone', models.CharField(max_length=11)),
                ('location', models.CharField(max_length=255)),
                ('qq', models.CharField(max_length=20)),
                ('weiChat', models.CharField(max_length=20)),
                ('company', models.CharField(max_length=50)),
            ],
        ),
    ]