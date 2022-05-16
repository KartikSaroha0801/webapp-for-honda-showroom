from django.http import HttpResponse
from django.shortcuts import render
from .forms import customer_form, staff_form

def homePage(request):
    return render(request, "homepage.html")

def cars_portal(request):
    return render(request, "cars_portal.html")

def honda_amaze(request):
    return render(request, "honda_amaze.html")

def honda_city(request):
    return render(request, "honda_city.html")

def honda_wrv(request):
    return render(request, "honda_wrv.html")

def staff_registration(request):
    fn=staff_form()
    data= {'form':fn}
    try:
        if request.method=="POST":
            n1= request.POST.get('staff name')
            n2= request.POST.get('Staff Address')
            n3= request.POST.get('Staff Pancard')
            n4= request.POST.get('Staff Aadhaar')
            n5= request.POST.get('Staff Phone Number')

            data={
                'form':fn,
                'n1':n1,
                'n2':n2,
                'n3':n3,
                'n4':n4,
                'n5':n5,

            }

    except:
        pass

    return render(request, "staff_registration.html", data)

def customer_registration(request):
    fx=customer_form()
    data= {'form':fx}
    try:
        if request.method=="POST":
            x1= request.POST.get('customer name')
            x2= request.POST.get('Customer Address')
            x3= request.POST.get('Customer Pancard')
            x4= request.POST.get('Cutomer Aadhaar No')
            x5= request.POST.get('Customer Phone No')

            data={
                'form':fx,
                'x1':x1,
                'x2':x2,
                'x3':x3,
                'x4':x4,
                'x5':x5,

            }

    except:
        pass

    return render(request, "customer_registration.html", data)

