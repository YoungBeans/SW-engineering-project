# Generated by Django 2.2.4 on 2019-11-27 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0009_auto_20191127_2241'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='reservCount',
            field=models.IntegerField(default=0),
        ),
    ]
