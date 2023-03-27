from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import auth, messages

from logbank.models import user_details


# Create your views here.
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['psw']
        c_password=request.POST['psw-repeat']
        if password==c_password:
            user=User.objects.create_user(username=username,password=password)
            user.save();

        else:
            messages.info(request,"password not matching")
            return redirect('register')
    return render(request,'register.html')


def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['psw']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,'login.html')
def new(request):
    return render(request,'newpage.html')

def add_userdetails(request):
    if request.method=='POST':
        username=request.POST['username']
        dob=request.POST['dob']
        age=request.POST['age']
        gender=request.POST['gender']
        phone_no=request.POST['phone_no']
        mail_id=request.POST['mail_id']
        district=request.POST['district']
        subdistrict=request.POST.get('subdistrict',False)
        accounttype=request.POST.get('accounttype',False)
        material_providing=request.POST.get('material_providing',False)
        details=user_details(username=username,dob=dob,age=age,gender=gender,phone_no=phone_no,mail_id=mail_id,district=district,subdistrict=subdistrict,accounttype=accounttype,material_providing=material_providing)
        details.save();
    messages.info(request,"Application sent successfully :)")
    return render(request,'userdetails.html')