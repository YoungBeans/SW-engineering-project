# Generated by Django 2.2.6 on 2019-12-01 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserv', '0009_auto_20191129_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='non_user_reservation',
            name='serial_number',
            field=models.CharField(default='WEBUIT3D', max_length=15),
        ),
    ]
