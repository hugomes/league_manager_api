# Generated by Django 4.1 on 2022-09-03 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_player_created_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='position',
        ),
        migrations.AddField(
            model_name='player',
            name='position',
            field=models.ManyToManyField(blank=True, null=True, related_name='position', to='base.position'),
        ),
    ]
