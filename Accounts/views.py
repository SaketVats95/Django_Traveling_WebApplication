from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate
from django.contrib import messages


# Create your views here.
def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        print(password1)
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Already Exists...')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Already Exists')
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email)
                user.set_password(password1)

                user.save()
                messages.info(request,'User Created')
                return redirect('/')
        else:
            messages.info(request,'Password Not Matching ....')
        return redirect('register')


    else:
        return render(request,"register.html")


def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        print(username,password)
        #u = User.objects.get(username__exact='jatin')
        #print(u.password)
        #u.set_password('11111')
        #u.save()
        #password='new password'
        user= authenticate(username=username,password=password)
        #print(user)
        if user is not None:
            auth.login(request,user)   
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
        

    else:
        return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')