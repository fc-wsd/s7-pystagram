# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-30 10:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0005_auto_20160930_1024'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='title',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]