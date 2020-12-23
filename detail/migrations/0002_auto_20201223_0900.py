# Generated by Django 3.1.4 on 2020-12-23 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detail', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='HotelImg',
            field=models.ImageField(blank=True, height_field=210, upload_to='', verbose_name='Фото отеля', width_field=210),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='HotelAdress',
            field=models.CharField(max_length=50, verbose_name='Адрес отеля'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='HotelName',
            field=models.CharField(max_length=50, verbose_name='Название отеля'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='HotelPrice',
            field=models.CharField(max_length=30, verbose_name='Цена отеля: от'),
        ),
    ]
