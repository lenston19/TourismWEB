# Generated by Django 3.1.4 on 2020-12-20 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HotelName', models.CharField(max_length=50)),
                ('HotelAdress', models.CharField(max_length=50)),
                ('HotelPrice', models.CharField(max_length=30)),
            ],
        ),
    ]
