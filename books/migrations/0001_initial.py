# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-13 15:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=254)),
                ('author', models.CharField(default='', max_length=254)),
                ('ISBN', models.CharField(default='', max_length=254)),
                ('date', models.DateTimeField()),
                ('notes', models.TextField()),
                ('image', models.ImageField(upload_to=None)),
            ],
        ),
    ]