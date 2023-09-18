import requests
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def register_view(request):

    if request.method == 'POST':
        username1 = request.POST.get('fullname')
        username2 = request.POST.get('username')
        username3 = request.POST.get('email')
        username4 = request.POST.get('password')
        username5 = request.POST.get('cpassword')
        if username4==username5:
            if User.objects.filter(username=username2).exists():
                messages.info(request,"user name already taken")
                return redirect('register')
            elif User.objects.filter(email=username3).exists():
                messages.info(request,"email already taken")
                return redirect('register')
            else:
                user=User.objects.create_user(first_name=username1,username=username2,email=username3,password=username4)
                user.save()
                return redirect('login')

                print('user initiated')
        else:
            messages.info(request,'password not matched')
            return redirect('register')
        return redirect('/')
    return render(request, 'register.html')
def login(request):
    if request.method == 'POST':
        username1=request.POST['username']
        pasword=request.POST["password"]
        user2=auth.authenticate(username=username1,password=pasword)
        if user2 is not None:
            auth.login(request,user2)
            return redirect('/')
        else:
            messages.info(request,'invalidlogin')
            return redirect('login')


    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')