# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-03 16:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weibook', '0014_auto_20170703_1550'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermodel',
            old_name='id',
            new_name='ui',
        ),
        migrations.AlterField(
            model_name='book',
            name='uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id', to='weibook.UserModel'),
        ),
    ]
