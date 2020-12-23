# Generated by Django 3.1.4 on 2020-12-23 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lk', '0001_initial'),
        ('detail', '0002_auto_20201223_0900'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='favorites_Hotel',
            field=models.ManyToManyField(blank=True, null=True, to='lk.User', verbose_name='Favorites'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='HotelImg',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фото отеля'),
        ),
    ]