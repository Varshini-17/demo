# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-12-28 14:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='password',
            field=models.CharField(max_length=20),
        ),
    ]
