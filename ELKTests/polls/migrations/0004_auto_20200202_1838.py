# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-02-02 18:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_session_simulation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='client_ip',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='simulation',
            name='client_ip',
            field=models.CharField(max_length=200),
        ),
    ]
