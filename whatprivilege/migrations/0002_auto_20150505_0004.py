# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('whatprivilege', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerTally',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('num_yes', models.IntegerField()),
                ('num_no', models.IntegerField()),
                ('question', models.ForeignKey(to='whatprivilege.Question')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='workshop',
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='helpLink',
            new_name='help_link',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='helpText',
            new_name='help_text',
        ),
        migrations.RemoveField(
            model_name='question',
            name='workshop_only',
        ),
        migrations.RemoveField(
            model_name='question',
            name='workshops',
        ),
        migrations.DeleteModel(
            name='Workshop',
        ),
    ]
