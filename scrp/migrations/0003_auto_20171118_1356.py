# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-18 21:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrp', '0002_auto_20171116_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='pat',
            field=models.FileField(upload_to=':\\home\\med\\main\\patterns'),
        ),
    ]
