# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0019_auto_20160926_1559'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='apiserver',
            options={'verbose_name': 'API\u540e\u53f0', 'verbose_name_plural': 'API\u540e\u53f0'},
        ),
        migrations.AlterModelOptions(
            name='apiuser',
            options={'verbose_name': 'API\u6388\u6743\u7528\u6237', 'verbose_name_plural': 'API\u6388\u6743\u7528\u6237'},
        ),
        migrations.AlterField(
            model_name='apiuser',
            name='user_phone',
            field=models.CharField(max_length=11),
        ),
    ]
