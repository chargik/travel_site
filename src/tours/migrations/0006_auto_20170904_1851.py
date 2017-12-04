# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 18:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0005_auto_20170829_1643'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tours',
            options={'ordering': ['-timestamp', '-updated'], 'verbose_name_plural': 'tours'},
        ),
        migrations.AddField(
            model_name='tours',
            name='included',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tours',
            name='not_included',
            field=models.TextField(blank=True, null=True),
        ),
    ]
