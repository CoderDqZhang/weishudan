# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-04 16:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weibook', '0017_auto_20170704_1618'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tagStr', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='tags',
        ),
        migrations.AddField(
            model_name='book',
            name='tags',
            field=models.ManyToManyField(related_name='tags', to='weibook.Tags'),
        ),
    ]
