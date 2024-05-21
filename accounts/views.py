from django.contrib import messages, auth
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


# Create your views here.

def Register_user(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        first_name=request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('password01')

        if password == cpassword:

            if User.objects.filter(username=username).exists():
                messages.info(request,'This username already exist')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'this mail already taken')
                return redirect('register')


            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                user.save()
            return redirect('login')
        else:
            messages.info(request,'this password not matching')
            return redirect('register')

    return render(request,'register.html')


def loginUser(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('home')

        else:
            messages.info(request,'Please Provide Correct Details')
            return redirect('login')



    return render(request,'login.html')


def logOut(request):
    auth.logout(request)
    return redirect('login')


def HomePage(request):
    return render(request,'home.html')