# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0014_auto_20160924_2224'),
    ]

    operations = [
        migrations.CreateModel(
            name='APIServer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('send_user', models.CharField(max_length=32)),
                ('email_subject', models.CharField(max_length=128)),
                ('to_email', models.EmailField(max_length=254)),
                ('email_content', models.TextField()),
                ('phone_number', models.IntegerField(max_length=11)),
                ('phone_content', models.CharField(max_length=64)),
                ('send_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='APIUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_email', models.EmailField(max_length=254)),
                ('user_phone', models.IntegerField(max_length=11)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
