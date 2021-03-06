# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-04 12:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20170528_2229'),
    ]

    operations = [
        migrations.AddField(
            model_name='manuscript',
            name='next',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prev', to='quiz.Manuscript'),
        ),
        migrations.AddField(
            model_name='manuscriptitem',
            name='action',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='from_item', to='quiz.ManuscriptItem'),
        ),
        migrations.AlterField(
            model_name='manuscript',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.Category'),
        ),
    ]
