# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-03 13:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fichas', '0006_auto_20170428_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='ficha',
            name='assunto1',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='ficha',
            name='assunto2',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='ficha',
            name='assunto3',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='ficha',
            name='assunto4',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='ficha',
            name='assunto5',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='ficha',
            name='figuras',
            field=models.CharField(choices=[('Sim', 'Sim'), ('Nao', 'Não')], default='Sim', max_length=20),
        ),
        migrations.AddField(
            model_name='ficha',
            name='folhas',
            field=models.PositiveIntegerField(default=1),
        ),
    ]