# Generated by Django 2.2.4 on 2019-11-27 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0010_user_reservcount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Point',
            fields=[
                ('normaluser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='login.NormalUser')),
                ('u_point', models.IntegerField(default=0)),
            ],
            bases=('login.normaluser',),
        ),
    ]