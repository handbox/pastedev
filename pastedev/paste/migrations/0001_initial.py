# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-19 07:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paste',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('title', models.CharField(blank=True, max_length=30)),
                ('syntax', models.IntegerField(choices=[(0, 'Plain'), (1, 'Python'), (2, 'HTML'), (3, 'SQL'), (4, 'Javascript'), (5, 'CSS')], default=0, max_length=30)),
                ('poster', models.CharField(blank=True, max_length=30)),
                ('timestamp', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
