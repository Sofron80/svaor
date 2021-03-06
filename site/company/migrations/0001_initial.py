# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-10 09:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Наименование категории')),
                ('slug', models.CharField(max_length=250, verbose_name='Наименование для ссылки')),
                ('keuw', models.CharField(blank=True, max_length=250, null=True, verbose_name='Ключевые слова')),
                ('desk', models.CharField(blank=True, max_length=250, null=True, verbose_name='Краткое описание')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'категории',
            },
        ),
    ]
