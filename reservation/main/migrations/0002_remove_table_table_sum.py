# Generated by Django 2.2.4 on 2019-11-08 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='table_sum',
        ),
    ]
