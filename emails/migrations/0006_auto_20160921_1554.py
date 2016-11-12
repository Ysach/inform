# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0005_emailinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailinfo',
            name='email',
            field=models.CharField(max_length=8000),
        ),
    ]
