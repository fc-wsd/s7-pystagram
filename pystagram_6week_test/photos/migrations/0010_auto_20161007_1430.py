# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-07 14:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0009_auto_20161007_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='%Y/%m/%d/'),
        ),
    ]