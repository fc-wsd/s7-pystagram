# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-01 06:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0005_auto_20160924_0742'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='%Y/%m/%d/'),
        ),
    ]
