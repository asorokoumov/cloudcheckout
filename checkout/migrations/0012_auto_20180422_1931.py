# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-04-22 16:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0011_auto_20180422_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
