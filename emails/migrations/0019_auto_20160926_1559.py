# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0018_auto_20160926_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apiserver',
            name='phone_number',
            field=models.CharField(max_length=11),
        ),
    ]
