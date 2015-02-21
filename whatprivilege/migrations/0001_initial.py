# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('questionText', models.TextField()),
                ('helpText', models.TextField()),
                ('helpLink', models.URLField()),
                ('numberYes', models.IntegerField()),
                ('numberNo', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('urlCode', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WorkshopQuestion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('workshopID', models.IntegerField()),
                ('qID', models.IntegerField()),
                ('numberYes', models.IntegerField()),
                ('numberNo', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
