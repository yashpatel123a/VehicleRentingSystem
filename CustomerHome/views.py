from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from CustomerHome.models import *
from Owner.models import Owner
from Manager.models import Manager
from Vehicles.models import Vehicle,Vehicle1
from RentVehicle.models import RentVehicle

from datetime import datetime
from datetime import date



isLogin = False
isLogout = False

# Create your views here.
def index(request):
    global isLogin
    global isLogout

    if('customeruser_email' in request.session):
        isLogin = True
        return redirect('/CustomerHome/')
        
    # vehicle = Vehicle.objects.all()
    if('customeruser_email' not in request.session and isLogout):
        isLogin = False
        isLogout = False
        Message = "Successfully Logged Out!!"
        # return render(request,'index.html',{'Message':Message,'vehicle':vehicle})
        return render(request,'index1.html',{'Message':Message})
    # return render(request,'index.html',{'vehicle':vehicle})
    return render(request,'index1.html')

def customersignin(request):
    return render(request,'CustomerSignIn.html')

def staffsignin(request):
    return render(request,'StaffSignIn.html')

def aboutus(request):
    return render(request,'aboutus.html')

def customerregister(request):
    return render(request,'CustomerRegister.html')


def CustomerLoginAuthentication(request):
    global isLogin
    login_email=request.POST.get('login_email','')
    login_password=request.POST.get('login_password','')
    # customer = Customer.objects.all()

    result_customer = Customers.objects.filter(customer_email=login_email,customer_password=login_password)

    if result_customer.exists():
        request.session['customeruser_email'] = login_email
        isLogin = True
        return redirect('/CustomerHome/')
    else:
        Message = "Invalid Email or password!!"
        return render(request,'CustomerSignIn.html',{'Message':Message})

def StaffLoginAuthentication(request):
    login_id=request.POST.get('login_email','')
    login_password=request.POST.get('login_password','')

    result_staff = Staffs.objects.filter(staff_id=login_id,staff_password=login_password)

    if result_staff.exists():
        request.session['staff_id'] = login_id
        return redirect('/StaffHome/')
    else:
        Message = "Invalid ID or password!!"
        return render(request,'StaffSignIn.html',{'Message':Message})


def CustomerRegisterCustomer(request):
    global isLogin

    customer_name=request.POST.get('name','')
    customer_email=request.POST.get('email','')
    customer_password=request.POST.get('password','')

    result_customer = Customers.objects.filter(customer_email=customer_email)

    if result_customer.exists():
        Message = "This Email address already exist!!"
        return render(request,'CustomerRegister.html',{'Message':Message})
    else:
        customer=Customers(customer_name=customer_name,customer_email=customer_email,
        customer_password=customer_password)
        
        customer.save()
        Message = "Successfully Registered, Please Log-in!!"
        return render(request,'CustomerSignIn.html',{'Message_success':Message})
        

def Logout(request):
    global isLogout
    del request.session['customeruser_email']
    isLogout = True
    Message = "Successfully Logged Out!!"
    return redirect('/')

def StaffLogout(request):
    del request.session['staff_id']
    Message = "Successfully Logged Out!!"
    return redirect('/')

def CustomerHome(request):
    if('customeruser_email' not in request.session):
        return redirect('/customersignin/')
    if isLogout:
        return redirect('/customersignin/')
    customer_email = request.session.get('customeruser_email')
    customer = Customers.objects.get(customer_email=customer_email)
    #vehicle = Vehicle.objects.all()
    #Message="Welcome Aboard!!"
    return render(request,'CustomerHome1.html',{'customer':customer})

def StaffHome(request):
    if('staff_id' not in request.session):
        return redirect('/staffsignin/')
    staff_id = request.session.get('staff_id')
    staff = Staffs.objects.get(staff_id=staff_id)
    return render(request,'StaffHome.html',{'staff':staff})


def Home(request):
    if('customeruser_email' not in request.session):
        return redirect('/customersignin/')
    customer_email = request.session.get('customeruser_email')
    customer = Customers.objects.get(customer_email=customer_email)
    vehicle = Vehicle.objects.all()
    return render(request,'CustomerHome.html',{'vehicle':vehicle,'customer':customer})


def BookVehicle(request):
    if('customeruser_email' not in request.session):
        return redirect('/customersignin/')
    customer_email = request.session.get('customeruser_email')
    customer = Customers.objects.get(customer_email=customer_email)
    vehicle = Vehicle1.objects.all()
    vehicle = vehicle.exclude(Vehicle_release_date__gte=date.today(),Vehicle_pickup_date__lte=date.today())
    return render(request,'bookvehicle.html',{'vehicle':vehicle,'customer':customer})

def FilterBookVehicle(request):
    if('customeruser_email' not in request.session):
        return redirect('/customersignin/')
    customer_email = request.session.get('customeruser_email')
    customer = Customers.objects.get(customer_email=customer_email)
    vehicles = Vehicle1.objects.all()
    vehicles = vehicles.exclude(Vehicle_release_date__gte=date.today(),Vehicle_pickup_date__lte=date.today())
    message = []
    vehicle = Vehicle1.objects.none()
    # print(request.POST.getlist('car'))
    # if request.POST.getlist('car') != []:
    #     vehicle = vehicles.filter(Vehicle_type='Car')
    #     message.append('car')
    # print(request.POST.getlist('two_wheeler'))
    # if request.POST.getlist('two_wheeler') != []:
    #     vehicle = vehicle.filter(Vehicle_type='Two wheeler')
    #     message.append('two_wheeler')
    # print(request.POST.getlist('bus'))
    # if request.POST.getlist('bus') != []:
    #     vehicle = vehicle.filter(Vehicle_type='Bus')
    #     message.append('bus')


    # print(request.POST.getlist('car'))
    # print(request.POST.getlist('two_wheeler'))
    # print(request.POST.getlist('bus'))
    if request.POST.getlist('car') != []:
        q = vehicles.filter(Vehicle_type='Car')
        vehicle = vehicle.union(q)
        message.append('car')
    if request.POST.getlist('two_wheeler') != []:
        q = vehicles.filter(Vehicle_type='Two wheeler')
        vehicle = vehicle.union(q)
        message.append('two_wheeler')
    if request.POST.getlist('bus') != []:
        q = vehicles.filter(Vehicle_type='Bus')
        vehicle = vehicle.union(q)
        message.append('bus')

    if request.POST.getlist('suzuki') != []:
        q = vehicles.filter(Vehicle_company='Suzuki')
        vehicle = vehicle.union(q)
        message.append('suzuki')
    if request.POST.getlist('honda') != []:
        q = vehicles.filter(Vehicle_company='Honda')
        vehicle = vehicle.union(q)
        message.append('honda')
    if request.POST.getlist('hyndai') != []:
        q = vehicles.filter(Vehicle_company='Hyundai')
        vehicle = vehicle.union(q)
        message.append('hyndai')
    if request.POST.getlist('volksvagen') != []:
        q = vehicles.filter(Vehicle_company='Volkswagen')
        vehicle = vehicle.union(q)
        message.append('volksvagen')
    if request.POST.getlist('tata') != []:
        q = vehicles.filter(Vehicle_company='Tata')
        vehicle = vehicle.union(q)
        message.append('tata')
    if request.POST.getlist('mahindra') != []:
        q = vehicles.filter(Vehicle_company='Mahindra')
        vehicle = vehicle.union(q)
        message.append('mahindra')
    if request.POST.getlist('volvo') != []:
        q = vehicles.filter(Vehicle_company='Volvo')
        vehicle = vehicle.union(q)
        message.append('volvo')

    if request.POST.getlist('1_2') != []:
        q = vehicles.filter(Vehicle_No_of_Seats__gte=1,Vehicle_No_of_Seats__lte=2)
        vehicle = vehicle.union(q)
        message.append('1_2')
    if request.POST.getlist('3_5') != []:
        q = vehicles.filter(Vehicle_No_of_Seats__gte=3,Vehicle_No_of_Seats__lte=5)
        vehicle = vehicle.union(q)
        message.append('3_5')
    if request.POST.getlist('6_8') != []:
        q = vehicles.filter(Vehicle_No_of_Seats__gte=6,Vehicle_No_of_Seats__lte=8)
        vehicle = vehicle.union(q)
        message.append('6_8')
    if request.POST.getlist('25') != []:
        q = vehicles.filter(Vehicle_No_of_Seats__gte=9)
        vehicle = vehicle.union(q)
        message.append('25')

    if request.POST.getlist('petrol') != []:
        q = vehicles.filter(Vehicle_fuel='Petrol')
        vehicle = vehicle.union(q)
        message.append('petrol')
    if request.POST.getlist('diesel') != []:
        q = vehicles.filter(Vehicle_fuel='Diesel')
        vehicle = vehicle.union(q)
        message.append('diesel')
    if request.POST.getlist('cng') != []:
        q = vehicles.filter(Vehicle_fuel='CNG')
        vehicle = vehicle.union(q)
        message.append('cng')
    if request.POST.getlist('electric') != []:
        q = vehicles.filter(Vehicle_fuel='Electric')
        vehicle = vehicle.union(q)
        message.append('electric')

    if request.POST.getlist('30') != []:
        q = vehicles.filter(Vehicle_price__lte=30)
        vehicle = vehicle.union(q)
        message.append('30')
    if request.POST.getlist('50') != []:
        q = vehicles.filter(Vehicle_price__lte=50)
        vehicle = vehicle.union(q)
        message.append('50')
    if request.POST.getlist('100') != []:
        q = vehicles.filter(Vehicle_price__lte=100)
        vehicle = vehicle.union(q)
        message.append('100')
    if request.POST.getlist('100+') != []:
        q = vehicles.filter(Vehicle_price__gt=100)
        vehicle = vehicle.union(q)
        message.append('100+')



    return render(request,'bookvehicle.html',{'vehicle':vehicle,'customer':customer,'message':message})



def Profile(request):
    if('user_email' not in request.session):
        return render(request,'CustomerSignIn.html')
    customer_email = request.session.get('user_email')
    customer = Customer.objects.get(customer_email=customer_email)
    return render(request,'Profile.html',{'customer':customer})

def showdetails(request,Vehicle_license_plate):
    if('customeruser_email' not in request.session):
        return render(request,'CustomerSignIn.html')
    vehicle = Vehicle1.objects.get(Vehicle_license_plate=Vehicle_license_plate)

    customer_email = request.session.get('customeruser_email')
    customer = Customers.objects.get(customer_email=customer_email)
    return render(request,'showdetails.html',{'vehicle':vehicle,'customer':customer})

def CheckAvailability(request,Vehicle_license_plate):
    if('user_email' not in request.session):
        return redirect('/signin/')

    RentVehicle_Date_of_Booking=request.POST.get('RentVehicle_Date_of_Booking','')
    RentVehicle_Date_of_Return=request.POST.get('RentVehicle_Date_of_Return','')
    
    RentVehicle_Date_of_Booking = datetime.strptime(RentVehicle_Date_of_Booking, '%Y-%m-%d').date()
    RentVehicle_Date_of_Return = datetime.strptime(RentVehicle_Date_of_Return, '%Y-%m-%d').date()

    rentvehicle = RentVehicle.objects.filter(Vehicle_license_plate=Vehicle_license_plate)
    vehicle = Vehicle.objects.get(Vehicle_license_plate=Vehicle_license_plate)

    customer_email = request.session.get('user_email')
    customer = Customer.objects.get(customer_email=customer_email)

    if RentVehicle_Date_of_Booking < date.today():
        Incorrect_dates = "Please give proper dates"
        return render(request,'showdetails_loggedin.html',{'Incorrect_dates':Incorrect_dates,'vehicle':vehicle,'customer':customer})

    if RentVehicle_Date_of_Return < RentVehicle_Date_of_Booking:
        Incorrect_dates = "Please give proper dates"
        return render(request,'showdetails_loggedin.html',{'Incorrect_dates':Incorrect_dates,'vehicle':vehicle,'customer':customer})
    
    days=(RentVehicle_Date_of_Return-RentVehicle_Date_of_Booking).days+1
    total=days*vehicle.Vehicle_price
    
    rent_data = {"RentVehicle_Date_of_Booking":RentVehicle_Date_of_Booking, "RentVehicle_Date_of_Return":RentVehicle_Date_of_Return,"days":days, "total":total}
    
    for rv in rentvehicle:

        if (rv.RentVehicle_Date_of_Booking >= RentVehicle_Date_of_Booking and RentVehicle_Date_of_Return >= rv.RentVehicle_Date_of_Booking) or (RentVehicle_Date_of_Booking >= rv.RentVehicle_Date_of_Booking and RentVehicle_Date_of_Return <= rv.RentVehicle_Date_of_Return) or (RentVehicle_Date_of_Booking <= rv.RentVehicle_Date_of_Return and RentVehicle_Date_of_Return >= rv.RentVehicle_Date_of_Return):
            if rv.isAvailable:
                Available = True
                Message = "Note that somebody has also requested for this vehicle from " + str(rv.RentVehicle_Date_of_Booking) + " to " + str(rv.RentVehicle_Date_of_Return)
                return render(request,'showdetails_loggedin.html',{'Message':Message,'Available':Available,'vehicle':vehicle,'customer':customer,'rent_data':rent_data})

            NotAvailable = True
            return render(request,'showdetails_loggedin.html',{'NotAvailable':NotAvailable,'dates':rv,'vehicle':vehicle,'customer':customer})

        # if (RentVehicle_Date_of_Booking < rv.RentVehicle_Date_of_Booking and RentVehicle_Date_of_Return < rv.RentVehicle_Date_of_Booking) or (RentVehicle_Date_of_Booking > rv.RentVehicle_Date_of_Return and RentVehicle_Date_of_Return > rv.RentVehicle_Date_of_Return):
        #     Available = True
        #     return render(request,'showdetails_loggedin.html',{'Available':Available,'vehicle':vehicle,'customer':customer,'rent_data':rent_data})


    Available = True
    return render(request,'showdetails_loggedin.html',{'Available':Available,'vehicle':vehicle,'customer':customer,'rent_data':rent_data})

def SentRequests(request):
    if('customeruser_email' not in request.session):
        return redirect('/customersignin/')

    customer_email = request.session.get('user_email')
    customer = Customers.objects.get(customer_email=customer_email)

    rentvehicle = RentVehicle.objects.filter(customer_email=customer_email)
    if rentvehicle.exists():
        vehicle = Vehicle.objects.all()
        return render(request,'SentRequests.html',{'customer':customer,'rentvehicle':rentvehicle,'vehicle':vehicle})
    else:
        Message = "You haven't rented any vehicle yet!!"
        return render(request,'SentRequests.html',{'customer':customer,'rentvehicle':rentvehicle,'Message':Message})



def sendrequest(request):

    

    customer_email = request.POST.get('customer_id','')
    customer = Customers.objects.get(customer_email=customer_email)

    vehicle_license_plate=request.POST.get('vehicle_id','')
    pickup_date=request.POST.get('pickupdate','')
    return_date=request.POST.get('returndate','')
    pickup_point=request.POST.get('pickuplocation','')
    mobile_no=request.POST.get('mno','')
    estimated_km=request.POST.get('km','')
    price = str(request.POST.get('price',''))
    price = int(price[1:])
    estimated_price=price


    ob=Requests(customer_email=Customers.objects.get(customer_email=customer_email),vehicle_license_plate=Vehicle1.objects.get(Vehicle_license_plate=vehicle_license_plate),pickup_date=pickup_date,return_date=return_date
        ,pickup_point=pickup_point,mobile_no=mobile_no,estimated_price=estimated_price,estimated_km=estimated_km)
        
    ob.save()
    Message = "Successfully Requested!!"
    requests = Requests.objects.filter(customer_email=Customers.objects.get(customer_email=customer_email))
    return render(request,'Pandingrequest.html',{'customer':customer,'Message':Message,'requests':requests})


def pendingrequests(request):
    if('customeruser_email' not in request.session):
        return redirect('/customersignin/')
    customer_email = request.session.get('customeruser_email')
    customer = Customers.objects.get(customer_email=customer_email)
    requests = Requests.objects.filter(customer_email=Customers.objects.get(customer_email=customer_email))
    return render(request,'Pandingrequest.html',{'customer':customer,'requests':requests})


def processpendingrequests(request):
    if('staff_id' not in request.session):
        return redirect('/staffsignin/')
    staff_id = request.session.get('staff_id')
    staff = Staffs.objects.get(staff_id=staff_id)
    requests = Requests.objects.all()
    driver = Drivers.objects.all()
    driver = driver.exclude(driver_release_date__gte=date.today(),driver_pickup_date__lte=date.today())
    
    return render(request,'ProcessPandingrequest.html',{'staff':staff,'requests':requests,'drivers':driver})


def process(request):
    if('staff_id' not in request.session):
        return redirect('/staffsignin/')
    
    staff_id = request.session.get('staff_id')
    staff = Staffs.objects.get(staff_id=staff_id)
    requests = Requests.objects.all()
    driver = Drivers.objects.all()

    

    customer_email = request.POST.get('customer_email','')
    vehicle_license_plate = request.POST.get('vehicle_license_plate','')
    mobile_no = request.POST.get('mobile_no','')
    pickup_date = request.POST.get('pickup_date','')
    return_date = request.POST.get('return_date','')
    pickup_point = request.POST.get('pickup_point','')
    estimated_km = request.POST.get('estimated_km','')
    estimated_price = request.POST.get('estimated_price','')

    dirver_id = request.POST.get('sd','')
    if dirver_id=='':
        remarks="No driver available."
        ob=Declinedrequests(customer_email=Customers.objects.get(customer_email=customer_email),vehicle_license_plate=Vehicle1.objects.get(Vehicle_license_plate=vehicle_license_plate)
            ,pickup_date=pickup_date,return_date=return_date,
        pickup_point=pickup_point,mobile_no=mobile_no,estimated_km=estimated_km,estimated_price=estimated_price,
        remarks=remarks)
        
        ob.save()
        Requests.objects.filter(customer_email=customer_email,
        vehicle_license_plate=vehicle_license_plate,mobile_no=mobile_no).delete()
        requests = Requests.objects.all()
        Message = "Declined the request!! No driver available."
        return render(request,'ProcessPandingrequest.html',{'staff':staff,'requests':requests,'drivers':driver,'Message':Message})

    vehicles = Vehicle1.objects.filter(Vehicle_license_plate=vehicle_license_plate)
    vehicles = vehicles.exclude(Vehicle_release_date__gte=date.today(),Vehicle_pickup_date__lte=date.today())
    if vehicles.exists():
        vehicles=Vehicle1.objects.get(Vehicle_license_plate=vehicle_license_plate)
        vehicles.Vehicle_pickup_date = pickup_date
        vehicles.Vehicle_release_date = return_date
        vehicles.save()
        d=Drivers.objects.get(dirver_id = dirver_id)
        d.driver_pickup_date = pickup_date
        d.driver_release_date = return_date
        d.save()
        
        ob=Approvedrequests(customer_email=Customers.objects.get(customer_email=customer_email),vehicle_license_plate=Vehicle1.objects.get(Vehicle_license_plate=vehicle_license_plate)
            ,pickup_date=pickup_date,return_date=return_date,
        pickup_point=pickup_point,mobile_no=mobile_no,estimated_km=estimated_km,estimated_price=estimated_price,
        dirver_id=dirver_id,driver_name=d.driver_name,driver_mobile_no=d.driver_mobile_no)
        ob.save()
        Requests.objects.filter(mobile_no=mobile_no).delete()
        requests = Requests.objects.all()
        driver = Drivers.objects.all()
        Message = "Approved request!!"
        return render(request,'ProcessPandingrequest.html',{'staff':staff,'requests':requests,'drivers':driver,'Message':Message})


    else:
        remarks="No vehicle available."
        ob=Declinedrequests(customer_email=Customers.objects.get(customer_email=customer_email),vehicle_license_plate=Vehicle1.objects.get(Vehicle_license_plate=vehicle_license_plate),pickup_date=pickup_date,return_date=return_date,
        pickup_point=pickup_point,mobile_no=mobile_no,estimated_km=estimated_km,estimated_price=estimated_price,
        remarks=remarks)
        
        ob.save()
        Requests.objects.filter(customer_email=customer_email,
        vehicle_license_plate=vehicle_license_plate,mobile_no=mobile_no).delete()
        requests = Requests.objects.all()
        Message = "Declined the request!! No vehicle available."
        return render(request,'ProcessPandingrequest.html',{'staff':staff,'requests':requests,'drivers':driver,'Message':Message})

    #return render(request,'ProcessPandingrequest.html',{'staff':staff,'requests':requests,'drivers':driver})


def showareqall(request):
    if('staff_id' not in request.session):
        return redirect('/staffsignin/')
    staff_id = request.session.get('staff_id')
    staff = Staffs.objects.get(staff_id=staff_id)
    
    arequests = Approvedrequests.objects.all()
    return render(request,'showareqall.html',{'staff':staff,'arequests':arequests})

def showrreqall(request):
    if('staff_id' not in request.session):
        return redirect('/staffsignin/')
    staff_id = request.session.get('staff_id')
    staff = Staffs.objects.get(staff_id=staff_id)
    
    rrequests = Declinedrequests.objects.all()
    return render(request,'showrreqall.html',{'staff':staff,'rrequests':rrequests})

def showareq(request):
    if('customeruser_email' not in request.session):
        return redirect('/customersignin/')
    customer_email = request.session.get('customeruser_email')
    customer = Customers.objects.get(customer_email=customer_email)

    arequests = Approvedrequests.objects.filter(customer_email=Customers.objects.get(customer_email=customer_email))
    
    return render(request,'showareq.html',{'customer':customer,'arequests':arequests})

def showrreq(request):
    

    if('customeruser_email' not in request.session):
        return redirect('/customersignin/')
    customer_email = request.session.get('customeruser_email')
    customer = Customers.objects.get(customer_email=customer_email)

    rrequests = Declinedrequests.objects.filter(customer_email=Customers.objects.get(customer_email=customer_email))
    
    return render(request,'showrreq.html',{'customer':customer,'rrequests':rrequests})


def about_us(request):
    return HttpResponse('About Us')
    
def contact_us(request):
    return HttpResponse('Contact Us')

def search(request):
    return HttpResponse('search')