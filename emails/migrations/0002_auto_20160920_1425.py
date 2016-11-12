# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emailuser',
            old_name='password',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='emailuser',
            old_name='username',
            new_name='subject',
        ),
        migrations.RemoveField(
            model_name='emailuser',
            name='phone',
        ),
        migrations.AddField(
            model_name='emailuser',
            name='content',
            field=models.CharField(default=None, max_length=600),
        ),
    ]
