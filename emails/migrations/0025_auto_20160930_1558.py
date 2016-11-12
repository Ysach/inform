# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0024_auto_20160930_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apiserver',
            name='phone_content',
            field=models.TextField(null=True, blank=True),
        ),
    ]
