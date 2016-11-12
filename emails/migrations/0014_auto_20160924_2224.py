# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0013_auto_20160924_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailinfo',
            name='username',
            field=models.CharField(max_length=64),
        ),
    ]
