# Generated by Django 4.1 on 2022-09-03 02:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_player_last_login_player_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='player',
            name='password',
        ),
    ]
