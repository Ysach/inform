# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0015_apiserver_apiuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apiserver',
            name='phone_number',
            field=models.IntegerField(),
        ),
    ]
