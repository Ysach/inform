# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0020_auto_20160926_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apiuser',
            name='user_phone',
            field=models.CharField(max_length=11, null=True),
        ),
    ]
