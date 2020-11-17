# Generated by Django 2.2.6 on 2019-11-02 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dsmr_datalogger', '0014_remove_optional_crc_check'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataloggersettings',
            name='dsmr_version',
            field=models.IntegerField(choices=[(4, 'Netherlands - DSMR version 4/5 (default)'), (3, 'Netherlands - DSMR version 2/3'), (101, 'Belgium - Fluvius (gas meter fix)'), (102, 'Luxembourg - Smarty (single tariff fix)')], default=4, help_text='The DSMR version your meter supports. Version should be printed on meter.', verbose_name='DSMR version'),
        ),
    ]
