# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-24 14:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jiaotongzhaoshi', '0012_auto_20171124_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jiaotongzhaoshi',
            name='AwardID',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='jiaotongzhaoshi',
            name='IndictmentID',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
