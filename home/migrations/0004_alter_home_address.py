# Generated by Django 4.2 on 2023-04-25 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_home_options_alter_home_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Manzil'),
        ),
    ]
