# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-15 22:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pagina", "0004_auto_20181114_0112"),
    ]

    operations = [
        migrations.AddField(
            model_name="presentation",
            name="is_favorite",
            field=models.BooleanField(default=False),
        ),
    ]
