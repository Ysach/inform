# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0012_emailinfo_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailinfo',
            name='username',
            field=models.CharField(default=b'farmer', max_length=64),
        ),
    ]
