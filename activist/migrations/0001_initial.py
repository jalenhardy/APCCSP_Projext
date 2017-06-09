# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 21:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('bio', models.TextField()),
                ('source', models.CharField(max_length=500)),
                ('date_recieved', models.DateField()),
                ('photo', models.TextField()),
                ('photos', models.TextField(default='None')),
                ('twitter_name', models.TextField(default='@Blklivesmatter')),
                ('youtube', models.CharField(default='None', max_length=5000)),
            ],
        ),
    ]