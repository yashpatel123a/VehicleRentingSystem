# Generated by Django 3.2.9 on 2021-12-19 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Vehicles', '0012_vehicle1'),
        ('CustomerHome', '0008_requests'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drivers',
            fields=[
                ('dirver_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('driver_name', models.CharField(max_length=100)),
                ('driver_password', models.CharField(max_length=100)),
                ('driver_pickup_date', models.DateField()),
                ('driver_release_date', models.DateField()),
                ('driver_mobile_no', models.CharField(max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='Staffs',
            fields=[
                ('staff_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('staff_name', models.CharField(max_length=100)),
                ('staff_password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Declinedrequests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pickup_date', models.DateField()),
                ('return_date', models.DateField()),
                ('pickup_point', models.CharField(max_length=200)),
                ('mobile_no', models.CharField(max_length=13)),
                ('estimated_km', models.IntegerField()),
                ('estimated_price', models.IntegerField()),
                ('remarks', models.CharField(max_length=100)),
                ('customer_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CustomerHome.customers')),
                ('vehicle_license_plate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vehicles.vehicle1')),
            ],
        ),
        migrations.CreateModel(
            name='Approvedrequests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pickup_date', models.DateField()),
                ('return_date', models.DateField()),
                ('pickup_point', models.CharField(max_length=200)),
                ('mobile_no', models.CharField(max_length=13)),
                ('estimated_km', models.IntegerField()),
                ('estimated_price', models.IntegerField()),
                ('dirver_id', models.CharField(max_length=100)),
                ('driver_name', models.CharField(max_length=100)),
                ('driver_mobile_no', models.CharField(max_length=13)),
                ('customer_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CustomerHome.customers')),
                ('vehicle_license_plate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vehicles.vehicle1')),
            ],
        ),
    ]
