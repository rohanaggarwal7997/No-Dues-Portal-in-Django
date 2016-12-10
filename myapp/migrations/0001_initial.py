# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-17 17:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rollno', models.CharField(max_length=9)),
                ('name', models.CharField(max_length=70)),
                ('webmail', models.CharField(max_length=30)),
                ('lab', models.BooleanField(default=0)),
                ('dept_library', models.BooleanField(default=0)),
                ('prof', models.BooleanField(default=0)),
                ('warden', models.BooleanField(default=0)),
            ],
        ),
    ]