# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-13 15:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='join',
            name='name',
        ),
        migrations.AddField(
            model_name='join',
            name='lead_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='join',
            name='telephone',
            field=models.CharField(blank=True, max_length=17),
        ),
    ]
