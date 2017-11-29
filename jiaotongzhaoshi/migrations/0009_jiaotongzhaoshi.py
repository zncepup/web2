# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-24 08:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('jiaotongzhaoshi', '0008_delete_jiaotongzhaoshi'),
    ]

    operations = [
        migrations.CreateModel(
            name='jiaotongzhaoshi',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('filename', models.CharField(blank=True, max_length=50, null=True)),
                ('AwardID', models.CharField(blank=True, max_length=30, null=True)),
                ('IndictmentID', models.CharField(blank=True, max_length=30, null=True)),
                ('TrialTime', models.CharField(blank=True, max_length=30, null=True)),
                ('Judge', models.CharField(blank=True, max_length=100, null=True)),
                ('Province', models.CharField(blank=True, max_length=30, null=True)),
                ('City', models.CharField(blank=True, max_length=30, null=True)),
                ('CountyDistrict', models.CharField(blank=True, max_length=30, null=True)),
                ('status', models.CharField(blank=True, max_length=10, null=True)),
                ('IncidentAge', models.IntegerField(blank=True, null=True)),
                ('EducationalBackground', models.CharField(blank=True, max_length=10, null=True)),
                ('pedigree', models.CharField(blank=True, max_length=1, null=True)),
                ('recividist', models.CharField(blank=True, max_length=1, null=True)),
                ('zishou', models.CharField(blank=True, max_length=1, null=True)),
                ('tanbai', models.CharField(blank=True, max_length=1, null=True)),
                ('ligong', models.CharField(blank=True, max_length=1, null=True)),
                ('renzui', models.CharField(blank=True, max_length=1, null=True)),
                ('huizui', models.CharField(blank=True, max_length=1, null=True)),
                ('keche', models.CharField(blank=True, max_length=1, null=True)),
                ('motuoche', models.CharField(blank=True, max_length=1, null=True)),
                ('huoche', models.CharField(blank=True, max_length=1, null=True)),
                ('jiaoche', models.CharField(blank=True, max_length=1, null=True)),
                ('diandongchejidong', models.CharField(blank=True, max_length=1, null=True)),
                ('baofeiche', models.CharField(blank=True, max_length=1, null=True)),
                ('taopaiche', models.CharField(blank=True, max_length=1, null=True)),
                ('qitajidongcheliang', models.CharField(blank=True, max_length=1, null=True)),
                ('feijidongche', models.CharField(blank=True, max_length=1, null=True)),
                ('Reaing', models.CharField(blank=True, max_length=1, null=True)),
                ('jiujia', models.CharField(blank=True, max_length=1, null=True)),
                ('zuijia', models.CharField(blank=True, max_length=1, null=True)),
                ('OverSpeed', models.CharField(blank=True, max_length=1, null=True)),
                ('OverLoad', models.CharField(blank=True, max_length=1, null=True)),
                ('DangerousCargo', models.CharField(blank=True, max_length=1, null=True)),
                ('Alcohol', models.CharField(blank=True, max_length=15, null=True)),
                ('Surveillans', models.CharField(blank=True, max_length=20, null=True)),
                ('Dentention', models.CharField(blank=True, max_length=20, null=True)),
                ('FixtedTerm', models.CharField(blank=True, max_length=20, null=True)),
                ('UnfixtedTerm', models.CharField(blank=True, max_length=20, null=True)),
                ('Death', models.CharField(blank=True, max_length=1, null=True)),
                ('LifeImprisonment', models.CharField(blank=True, max_length=1, null=True)),
                ('Fine', models.CharField(blank=True, max_length=20, null=True)),
                ('ConfiscationOfProperty', models.CharField(blank=True, max_length=1, null=True)),
                ('DeprivalOfPoliticalRight', models.CharField(blank=True, max_length=1, null=True)),
                ('Deportation', models.CharField(blank=True, max_length=1, null=True)),
                ('CaptureIllegalProperty', models.CharField(blank=True, max_length=1, null=True)),
                ('DeathNum', models.IntegerField(blank=True, null=True)),
                ('InjuredNum', models.IntegerField(blank=True, null=True)),
                ('DegreeOfPropertyLosses', models.CharField(blank=True, max_length=100, null=True)),
                ('AmountOfCompensation', models.CharField(blank=True, max_length=30, null=True)),
                ('VictimUnderstanding', models.CharField(blank=True, max_length=3, null=True)),
                ('confirmationOfResponsibility', models.CharField(blank=True, max_length=4, null=True)),
                ('Abscond', models.CharField(blank=True, max_length=3, null=True)),
                ('DeathCausedByAbscond', models.CharField(blank=True, max_length=3, null=True)),
            ],
        ),
    ]
