# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0004_userauth'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject', models.CharField(max_length=64)),
                ('email', models.CharField(max_length=64)),
                ('content', models.CharField(max_length=600)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
