# Generated by Django 4.2.9 on 2024-01-26 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testbeds', '0006_testbed_device_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testbed',
            name='device_type',
            field=models.TextField(default='ftd'),
        ),
    ]
