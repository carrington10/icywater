# Generated by Django 2.0.1 on 2018-07-23 12:11

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('icyWater', '0002_musicpost_music'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MusicPost',
            new_name='Songs',
        ),
    ]
