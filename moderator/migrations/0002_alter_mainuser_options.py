# Generated by Django 4.2 on 2023-04-25 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moderator', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mainuser',
            options={'verbose_name': 'User', 'verbose_name_plural': 'Userlar'},
        ),
    ]
