# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-08 01:51
from __future__ import unicode_literals

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160808_0112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(upload_to=blog.models.myupload_to),
        ),
    ]
