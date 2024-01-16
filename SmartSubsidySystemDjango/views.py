from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from service.models import Contact, Schemesinfo, Applications
from django.shortcuts import render

@login_required
def Home(request):
    return render(request, 'Home.html', {})

def Register(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        phno = request.POST.get('number')
        password = request.POST.get('password')

        new_user = User.objects.create_user(name, email, password)
        new_user.phno = phno

        new_user.save()
        return redirect('loginpage')
    return render(request,'Register.html', {})

def Login(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            return HttpResponse('Error, user does not exist')
    return render(request,'Login.html', {})

def logoutuser(request):
    logout(request)
    return redirect('loginpage')


def Aboutus(request):
    return render(request,'Aboutus.html', {})

def Contactus(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        ins = Contact(name=name, email=email, message=message)
        ins.save()
        print("ok")   
    return render(request,'contactus.html', {})

def Services(request):
    return render(request,'Services.html', {})

def Scheme1(request):
    return render(request,'scheme1.html', {})

def Dash(request):
    dashdata = Schemesinfo.objects.all()
    if request.method=="GET":
        se=request.GET.get('searchname')
        if se!=None:
            dashdata = Schemesinfo.objects.filter(schemename__icontains=se)
    context = {'dash': dashdata}
    return render(request, 'Schemesinfo.html', context)

def Applicationform(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        lastname = request.POST['lastname']
        date_of_birth = request.POST['date_of_birth']
        citizensip = request.POST['citizensip']
        state = request.POST['state']
        age = request.POST['age']
        gender = request.POST['gender']
        caste = request.POST['caste']
        rationcard = request.POST['rationcard']
        employmentStatus = request.POST['employmentStatus']
        aadhaarnumber = request.POST['aadhaarnumber']
        schemename = request.POST['schemename']

        ins = Applications(first_name=first_name, lastname=lastname, date_of_birth=date_of_birth, citizensip=citizensip, 
                               state=state, age=age, gender=gender, caste=caste, rationcard=rationcard, employmentStatus=employmentStatus,
                                 aadhaarnumber=aadhaarnumber, schemename=schemename)
        ins.save()
        print("ok")
    return render(request,'Applicationform.html', {})

def Approval(request):
    # Fetch only approved Applicationform
    approved_applicationform = Applications.objects.filter(is_approved=True)

    context = {'approved_applicationform': approved_applicationform}
    return render(request, 'Approval.html', context)

def subsidy_view(request):
    return render(request, 'subsidy.html')    

