# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-10 21:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Empinf', '0003_auto_20180210_2159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='dept',
        ),
    ]
