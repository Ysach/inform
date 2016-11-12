# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0008_msginfo_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='msginfo',
            name='email',
            field=models.ForeignKey(to='emails.EmailInfo'),
        ),
    ]
