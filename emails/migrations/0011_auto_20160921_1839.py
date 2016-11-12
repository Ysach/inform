# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0010_remove_msginfo_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='msginfo',
            old_name='content',
            new_name='msg',
        ),
    ]
