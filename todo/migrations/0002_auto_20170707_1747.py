# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-07 17:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='date updated'),
        ),
    ]
