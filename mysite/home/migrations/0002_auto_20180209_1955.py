# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-10 00:55
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feature',
            name='foreign_id',
        ),
        migrations.AddField(
            model_name='feature',
            name='foreign_reference_number',
            field=models.CharField(default='abc', max_length=6, unique=True, validators=[django.core.validators.MinLengthValidator(6)]),
            preserve_default=False,
        ),
    ]