# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-22 16:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20161119_1327'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='hostelC',
            new_name='hostelValC',
        ),
        migrations.AddField(
            model_name='student',
            name='hostelVal',
            field=models.BooleanField(default=1),
        ),
    ]