# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-18 13:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fichas', '0009_auto_20170517_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='ficha',
            name='instituicao',
            field=models.CharField(default='Faculdade Serra do Carmo', max_length=200),
        ),
    ]
