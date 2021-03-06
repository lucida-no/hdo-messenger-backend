# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-31 21:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0031_auto_20171022_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manuscriptitem',
            name='type',
            field=models.CharField(choices=[('text', 'Text'), ('quick_reply', 'Quick reply'), ('url', 'URL'), ('quiz_result', 'Quiz: Show result'), ('quiz_q_promises_checked', 'Quiz: Show checked promise questions'), ('quiz_level', 'Quiz: Show level select'), ('quiz_categories', 'Quiz: Show category select'), ('quiz_question', 'Quiz: Show party question'), ('quiz_question_select', 'Quiz: Select random unanswered question'), ('quiz_generic_question', 'Quiz: Show question'), ('quiz_yes_or_no_question', 'Quiz: Show yes or no question'), ('vg_result', 'Voter guide: Show result'), ('vg_categories', 'Voter guide: Show category select'), ('vg_questions', 'Voter guide: Show questions')], default='text', max_length=100),
        ),
    ]
