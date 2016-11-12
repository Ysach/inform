# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0011_auto_20160921_1839'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailinfo',
            name='username',
            field=models.CharField(default=None, max_length=64),
        ),
    ]
