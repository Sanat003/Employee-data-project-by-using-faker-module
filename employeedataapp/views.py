from django.http import HttpResponse
from django.shortcuts import render
import faker
fake=faker.Faker()
from .models import EmployeeData

def employeedataview(request):
    for i in range(200):
        EmployeeData(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        emaill=fake.email(),
        salary=fake.random_element(elements=(10000,20000,30000,40000)),
        company=fake.random_element(elements=('TCS','HCL','INFOSYS','IBM','ACCENTURE')),
        location=fake.random_element(elements=('Hyderabad','Bangalore','Chennai','Delhi')),
        adress=fake.address()

        ).save()
    return HttpResponse("Data Saved")

def fetchingalldata(request):
    employees=EmployeeData.objects.all()
    return render(request,'employeealldata.html',{'employees':employees})

def mainpage(request):
    return render(request,'mainpage.html')

def hyderabaddata(request):
    if request.method == 'GET':
        hydData=EmployeeData.objects.filter(location='Hyderabad')
        return render(request,'hydData.html',{'hydData':hydData})
    else:
        company=request.POST.get('company')
        hydData=EmployeeData.objects.filter(location='Hyderabad') & EmployeeData.objects.filter(company=company)
        return render(request,'hydData.html',{'hydData':hydData})

def bangaloredata(request):
    bangData=EmployeeData.objects.filter(location='Bangalore')
    return render (request,'bangData.html',{'bangData':bangData})

def chennaidata(request):
    cheData=EmployeeData.objects.filter(location='Chennai')
    return render(request,'cheData.html',{'cheData':cheData})

def delhidata(request):
    delData=EmployeeData.objects.filter(location='Delhi')
    return render(request,'delData.html',{'delData':delData})
