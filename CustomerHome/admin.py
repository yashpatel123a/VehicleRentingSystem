from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Customer)
admin.site.register(Customers)
admin.site.register(Requests)
admin.site.register(Drivers)
admin.site.register(Staffs)
admin.site.register(Approvedrequests)
admin.site.register(Declinedrequests)