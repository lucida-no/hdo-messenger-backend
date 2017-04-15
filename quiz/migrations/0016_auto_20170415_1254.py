# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-15 12:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0015_auto_20170325_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='correct_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='manuscriptitem',
            name='type',
            field=models.CharField(choices=[('button', 'Button'), ('promises', 'Promises'), ('quiz_result', 'Quiz results'), ('text', 'Text'), ('url', 'URL')], default='text', max_length=100),
        ),
    ]
