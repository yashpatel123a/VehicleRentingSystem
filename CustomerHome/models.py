from django.db import models
from Vehicles.models import Vehicle1

# Create your models here.
class Customer(models.Model):
    customer_id = models.AutoField
    customer_firstname = models.CharField(max_length=60)
    customer_lastname = models.CharField(max_length=60)
    customer_address = models.CharField(max_length=600)
    customer_email = models.CharField(max_length=100)
    customer_password = models.CharField(max_length=32)
    customer_dob = models.DateField()
    customer_mobileno = models.CharField(max_length=10)
    customer_gender = models.CharField(max_length=15)
    customer_license = models.ImageField(upload_to='img/Customer_License/')
    customer_city = models.CharField(max_length=30)
    customer_state = models.CharField(max_length=30)
    customer_country = models.CharField(max_length=30)
    customer_pincode = models.IntegerField()

    def __str__(self):
        return self.customer_email + ": " + str(self.customer_license)


class Customers(models.Model):
    customer_email = models.CharField(max_length=100, primary_key=True)
    customer_password = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=100)
    def __str__(self):
        return self.customer_email


class Staffs(models.Model):
    staff_id = models.CharField(max_length=100, primary_key=True)
    staff_name = models.CharField(max_length=100)
    staff_password = models.CharField(max_length=100)


class Drivers(models.Model):
    dirver_id = models.CharField(max_length=100, primary_key=True)
    driver_name = models.CharField(max_length=100)
    driver_password = models.CharField(max_length=100)
    driver_pickup_date = models.DateField()
    driver_release_date = models.DateField()
    driver_mobile_no = models.CharField(max_length=13)



class Requests(models.Model):
    request_id = models.AutoField
    customer_email = models.ForeignKey(Customers,on_delete=models.CASCADE)
    vehicle_license_plate = models.ForeignKey(Vehicle1,on_delete=models.CASCADE)
    pickup_date = models.DateField()
    return_date = models.DateField()
    pickup_point = models.CharField(max_length=200)
    mobile_no = models.CharField(max_length=13)
    estimated_km = models.IntegerField()
    estimated_price = models.IntegerField()


class Approvedrequests(models.Model):
    customer_email = models.ForeignKey(Customers,on_delete=models.CASCADE)
    vehicle_license_plate = models.ForeignKey(Vehicle1,on_delete=models.CASCADE)
    pickup_date = models.DateField()
    return_date = models.DateField()
    pickup_point = models.CharField(max_length=200)
    mobile_no = models.CharField(max_length=13)
    estimated_km = models.IntegerField()
    estimated_price = models.IntegerField()
    dirver_id = models.CharField(max_length=100)
    driver_name = models.CharField(max_length=100)
    driver_mobile_no = models.CharField(max_length=13)

class Declinedrequests(models.Model):
    customer_email = models.ForeignKey(Customers,on_delete=models.CASCADE)
    vehicle_license_plate = models.ForeignKey(Vehicle1,on_delete=models.CASCADE)
    pickup_date = models.DateField()
    return_date = models.DateField()
    pickup_point = models.CharField(max_length=200)
    mobile_no = models.CharField(max_length=13)
    estimated_km = models.IntegerField()
    estimated_price = models.IntegerField()
    remarks = models.CharField(max_length=100)

    


