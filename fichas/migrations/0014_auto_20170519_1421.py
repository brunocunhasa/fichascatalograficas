# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-19 14:21
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fichas', '0013_auto_20170518_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ficha',
            name='tamanho_fonte',
            field=models.PositiveIntegerField(default=11, validators=[django.core.validators.MaxValueValidator(14), django.core.validators.MinValueValidator(9)]),
        ),
    ]
