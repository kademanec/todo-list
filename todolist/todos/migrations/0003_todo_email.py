# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-18 06:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_auto_20190408_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]