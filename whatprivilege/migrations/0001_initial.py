# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('yes', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('helpText', models.TextField(blank=True)),
                ('helpLink', models.URLField(blank=True)),
                ('workshop_only', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=255, null=True, blank=True)),
                ('title', models.TextField(max_length=255, null=True, blank=True)),
                ('description', models.TextField(max_length=255, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='question',
            name='workshops',
            field=models.ManyToManyField(related_name=b'questions', null=True, to='whatprivilege.Workshop', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(to='whatprivilege.Question'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='workshop',
            field=models.ForeignKey(default=None, blank=True, to='whatprivilege.Workshop', null=True),
            preserve_default=True,
        ),
    ]
