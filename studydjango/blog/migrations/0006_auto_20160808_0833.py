# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-08 08:33
from __future__ import unicode_literals

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_comment_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='image',
            field=models.ImageField(null=True, upload_to=blog.models.myupload_to),
        ),
    ]
