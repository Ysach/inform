# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0025_auto_20160930_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apiserver',
            name='email_subject',
            field=models.CharField(max_length=255),
        ),
    ]
