# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-25 03:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0008_tovar_nalich'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='keuw',
            new_name='keyw',
        ),
    ]