# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-16 13:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='pat',
            field=models.FileField(upload_to='home/med/main/patterns'),
        ),
    ]
