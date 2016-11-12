# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0007_msginfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='msginfo',
            name='email',
            field=models.ForeignKey(default=None, to='emails.EmailInfo'),
        ),
    ]
