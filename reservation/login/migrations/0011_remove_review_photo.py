# Generated by Django 2.2.6 on 2019-12-01 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0010_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='photo',
        ),
    ]
