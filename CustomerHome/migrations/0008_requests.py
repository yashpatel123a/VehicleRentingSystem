# Generated by Django 3.2.9 on 2021-12-19 06:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Vehicles', '0012_vehicle1'),
        ('CustomerHome', '0007_auto_20211117_1301'),
    ]

    operations = [
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pickup_date', models.DateField()),
                ('return_date', models.DateField()),
                ('pickup_point', models.CharField(max_length=200)),
                ('mobile_no', models.CharField(max_length=13)),
                ('estimated_km', models.IntegerField()),
                ('estimated_price', models.IntegerField()),
                ('customer_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CustomerHome.customers')),
                ('vehicle_license_plate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vehicles.vehicle1')),
            ],
        ),
    ]