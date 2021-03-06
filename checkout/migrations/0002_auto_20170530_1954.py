# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-30 16:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_service', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('image', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=200)),
                ('development', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameField(
            model_name='seller',
            old_name='name',
            new_name='login',
        ),
        migrations.RemoveField(
            model_name='seller',
            name='created_date',
        ),
        migrations.AddField(
            model_name='seller',
            name='password',
            field=models.CharField(default=123, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seller',
            name='phone',
            field=models.CharField(default=79161234567, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checkout.Seller'),
        ),
        migrations.AddField(
            model_name='delivery',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checkout.Product'),
        ),
    ]
