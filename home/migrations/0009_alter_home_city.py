# Generated by Django 4.2 on 2023-05-13 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_home_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='city',
            field=models.CharField(choices=[('Andijan', 'Andijan'), ('Bukhara', 'Bukhara'), ('Fergana', 'Fergana'), ('Jizzakh', 'Jizzakh'), ('Khorezm', 'Khorezm'), ('Namangan', 'Namangan'), ('Navoiy', 'Navoiy'), ('Qashqadaryo', 'Qashqadaryo'), ('Samarqand', 'Samarqand'), ('Sirdaryo', 'Sirdaryo'), ('Surxondaryo', 'Surxondaryo'), ('Tashkent', 'Tashkent'), ('Xorazm', 'Xorazm'), ("Qoraqalpog'iston", "Qoraqalpog'iston")], default='Tashkent', max_length=100, verbose_name='Shahar'),
        ),
    ]
