# Generated by Django 2.2.6 on 2019-12-01 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserv', '0012_merge_20191201_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='non_user_reservation',
            name='serial_number',
            field=models.CharField(default='OJBJ4Y2S', max_length=15),
        ),
    ]