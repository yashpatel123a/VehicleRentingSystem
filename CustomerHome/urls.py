from django.urls import path
from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include

urlpatterns = [
    path('', views.index, name="Home"),
    path('Home/', views.Home, name="LoggedinHome"),
    path('CustomerHome/', views.CustomerHome, name="LoggedinHome"),

    path('bookvehicle/',views.BookVehicle, name="BookVehicle"),
    path('filterbookvehicle/',views.FilterBookVehicle, name="FilterBookVehicle"),

    path('aboutus/',views.aboutus,name="aboutus"),
    path('customersignin/',views.customersignin,name="CustomerSignIn"),
    path('Logout/',views.Logout,name="Logout"),    
    path('customerregister/',views.customerregister,name="CustomerRegister"),
    path('CustomerLoginAuthentication/',views.CustomerLoginAuthentication,name="CustomerLoginAuthentication"),
    path('CustomerRegisterCustomer/',views.CustomerRegisterCustomer,name="CustomerRegisterCustomer"),

    path('sendrequest/',views.sendrequest,name='sendrequest'),
    path('pendingrequests/',views.pendingrequests,name='pendingrequests'),

    path('Profile/',views.Profile,name="Profile"),
    path('about/', views.about_us, name="AboutUs"),
    path('contact/', views.contact_us, name="ContactUs"),
    path('search/', views.search, name="Search"),

    path('VehicleDetails/<str:Vehicle_license_plate>/',views.showdetails,name="VehicleDetails"),
    
    path('CheckAvailability/<str:Vehicle_license_plate>/',views.CheckAvailability,name="CheckAvailability"),
    path('SentRequests/',views.SentRequests,name="SentRequests"),
    path('RentVehicle',include("RentVehicle.urls")),
    path('Owner/',include("Owner.urls")),
    path('Manager/',include("Manager.urls")),


    path('staffsignin/',views.staffsignin,name="StaffSignIn"),
    path('StaffLoginAuthentication/',views.StaffLoginAuthentication,name="StaffLoginAuthentication"),
    path('StaffHome/', views.StaffHome, name="LoggedinHome"),
    path('StaffLogout/',views.StaffLogout,name="Logout"),
    path('processpendingrequests/',views.processpendingrequests,name='processpendingrequests'),
    path('process/',views.process,name='process'),

    path('showareqall/',views.showareqall,name="showareqall"),
    path('showrreqall/',views.showrreqall,name="showrreqall"),
    path('showareq/',views.showareq,name="showareq"),
    path('showrreq/',views.showrreq,name="showrreq")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL ,document_root=settings.MEDIA_ROOT)