# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-21 21:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dsmr_datalogger', '0005_verify_telegram_crc_setting'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dataloggersettings',
            name='track_meter_statistics',
        ),
        migrations.AlterField(
            model_name='dataloggersettings',
            name='dsmr_version',
            field=models.IntegerField(choices=[(4, 'DSMR version 4+'), (3, 'DSMR version 2')], default=4, help_text='The DSMR version your meter supports. Version should be printed on meter.', verbose_name='DSMR version'),
        ),
        migrations.AlterField(
            model_name='meterstatistics',
            name='timestamp',
            field=models.DateTimeField(auto_now=True, help_text='Timestamp indicating when the reading was taken'),
        ),
        migrations.AddField(
            model_name='meterstatistics',
            name='dsmr_version',
            field=models.CharField(default=None, help_text='DSMR version', max_length=2, null=True),
        ),
    ]