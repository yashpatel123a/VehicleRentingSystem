# Generated by Django 3.2.9 on 2021-12-11 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vehicles', '0009_auto_20211212_0056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle1',
            name='Vehicle_image1',
            field=models.ImageField(upload_to='img/Vehicle_images/'),
        ),
        migrations.AlterField(
            model_name='vehicle1',
            name='Vehicle_image2',
            field=models.ImageField(upload_to='img/Vehicle_images/'),
        ),
        migrations.AlterField(
            model_name='vehicle1',
            name='Vehicle_image3',
            field=models.ImageField(upload_to='img/Vehicle_images/'),
        ),
    ]