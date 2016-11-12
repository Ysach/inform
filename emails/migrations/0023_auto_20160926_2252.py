# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0022_auto_20160926_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apiuser',
            name='user_email',
            field=models.EmailField(unique=True, max_length=254),
        ),
    ]
