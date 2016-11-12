# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0017_auto_20160926_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apiserver',
            name='phone_number',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='apiuser',
            name='user_phone',
            field=models.IntegerField(default=None),
        ),
    ]
