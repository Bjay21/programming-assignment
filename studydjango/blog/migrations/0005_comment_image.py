# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-08 08:06
from __future__ import unicode_literals

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20160808_0151'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='image',
            field=models.ImageField(default='', upload_to=blog.models.myupload_to),
            preserve_default=False,
        ),
    ]
