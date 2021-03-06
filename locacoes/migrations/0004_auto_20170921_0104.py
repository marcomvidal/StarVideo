# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-21 04:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locacoes', '0003_remove_filme_preco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filme',
            name='capa',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='filme',
            name='data_lancamento',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='filme',
            name='sinopse',
            field=models.TextField(blank=True, default=''),
        ),
    ]
