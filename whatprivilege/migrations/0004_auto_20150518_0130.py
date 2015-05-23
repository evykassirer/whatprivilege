# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('whatprivilege', '0003_auto_20150518_0111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='visitor',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
