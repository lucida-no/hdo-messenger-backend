# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-15 13:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0020_auto_20170415_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answerset',
            name='session',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='answers', to='messenger_bot.ChatSession'),
        ),
    ]
