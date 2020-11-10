from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate,logout,login
from .models import *

# Create your views here.
def Login(request):
    dic={'err':''}
    if request.method=='POST':
        d=request.POST
        u=d['u']
        p=d['p']
        if authenticate(username=u,password=p):
            login(request,authenticate(username=u,password=p))
            return redirect('dashboard')
        else:
            dic={'err':'* incorrect username or password'}
    return render(request,'Login.html',dic)

def register(request):
    dic={'err':''}
    if request.method=='POST':
        d=request.POST
        u=d['u']
        dob=d['dob']
        e=d['e']
        p=d['p']
        cp=d['cp']
        if len(u)<6:
            dic={'err':'* invalid username'}
            return render(request, 'Register.html', dic)
        if len(p)<6:
            dic = {'err': '* invalid password'}
            return render(request, 'Register.html', dic)
        if p!=cp:
            dic = {'err': '* password mismatch'}
            return render(request, 'Register.html', dic)
        try:
            User.objects.create_user(username=u,password=p,email=e)
            Profile.objects.create(user=authenticate(username=u,password=p),dob=dob)
        except:
            dic = {'err': '* Already registered'}
            return render(request, 'Register.html', dic)
        return redirect('login')
    return render(request,'Register.html',dic)

def Logout(request):
    logout(request)
    return redirect('login')

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.conf import settings

def forget(request):
    dic={'err':'','email':''}
    if request.method=='POST':
        d=request.POST
        email=d['e']
        try:
            user=User.objects.get(email=email)
            print(user.email)
            try:
                from_email = settings.EMAIL_HOST_USER
                to_email = user.email
                sub = "Blog Added"
                msg = EmailMultiAlternatives(sub, '', from_email, [to_email])
                dic = {"title": '5690', "des": user.username}
                html = get_template('mail.html').render(dic)
                msg.attach_alternative(html, 'text/html')
                msg.send()
                return render(request,'OTP.html',{'email':email})
            except:
                dic = {'err': '*something went wrong ,try angain.','email':''}
        except:
            dic = {'err': '*email id not registered.','email':''}

    return render(request,'Forget.html',dic)

def dashboard(request):
    u=User.objects.get(username=request.user.username)
    p=Profile.objects.get(user=u)
    dic={'obj':p}
    return render(request,'Dashboard.html',dic)

def update(request):
    if request.method=='POST':
        i=request.FILES['i']
        u = User.objects.get(username=request.user.username)
        p = Profile.objects.get(user=u)
        p.image=i
        p.save()
        return redirect('dashboard')
    return render(request,'Update.html')

def changepass(request,e):
    if request.method=='POST':

        d=request.POST
        otp=d['otp']
        if otp=='5690':
            return render(request,'ChangePass.html',{'email':e,'err':''})
        else:
            return HttpResponse('incorrect otp')
    return HttpResponse('Somthing went wrong')

def cpass(request,e):
    if request.method=='POST':
        d=request.POST
        p=d['p']
        cp=d['cp']
        if p!=cp:
            return render(request, 'ChangePass.html', {'email': e, 'err': '* mismatch password'})
        else:
            user = User.objects.get(email=e)
            user.set_password(p)
            user.save()
            return redirect('login')
