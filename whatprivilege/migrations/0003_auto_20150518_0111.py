# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('whatprivilege', '0002_auto_20150505_0004'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('yes', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('question', models.ForeignKey(to='whatprivilege.Question')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='answertally',
            name='question',
        ),
        migrations.DeleteModel(
            name='AnswerTally',
        ),
        migrations.AddField(
            model_name='answer',
            name='visitor',
            field=models.ForeignKey(to='whatprivilege.Visitor'),
            preserve_default=True,
        ),
    ]
