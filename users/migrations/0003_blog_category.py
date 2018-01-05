# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-17 12:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20171216_2216'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.CharField(choices=[('bk', '博客'), ('essay', '随笔')], default='bk', max_length=2, verbose_name='类别'),
        ),
    ]
