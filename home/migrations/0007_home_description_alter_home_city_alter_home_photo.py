# Generated by Django 4.2 on 2023-05-02 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_home_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='description',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='home',
            name='city',
            field=models.CharField(choices=[('Andijan', 'Andijan'), ('Bukhara', 'Bukhara'), ('Fergana', 'Fergana'), ('Jizzakh', 'Jizzakh'), ('Khorezm', 'Khorezm'), ('Namangan', 'Namangan'), ('Navoiy', 'Navoiy'), ('Qashqadaryo', 'Qashqadaryo'), ('Samarqand', 'Samarqand'), ('Sirdaryo', 'Sirdaryo'), ('Surxondaryo', 'Surxondaryo'), ('Tashkent', 'Tashkent'), ('Xorazm', 'Xorazm')], default='Tashkent', max_length=100, verbose_name='Shahar'),
        ),
        migrations.AlterField(
            model_name='home',
            name='photo',
            field=models.ImageField(default='images/home/default.png', upload_to='images/home'),
        ),
    ]
