# Generated by Django 4.1 on 2022-09-02 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_team_position_player_position_player_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='player',
            name='password',
            field=models.CharField(default=123, max_length=50),
        ),
    ]