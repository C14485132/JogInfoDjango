# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-12 15:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('JogInfo', '0002_auto_20171212_1512'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datapoint',
            old_name='run',
            new_name='jog',
        ),
    ]