from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from .models import *

# Create your views here.
def Login(request):
    er={'er':False}
    if request.method=='POST':
        d=request.POST
        user=d['u']
        p=d['p']
        if authenticate(username=user,password=p):
            return redirect('slist')
        else:
            er={'er':True}
    return render(request,'Login.html',er)

def subjects(request):
    d=Subject.objects.all()
    dict={'sub':d}
    return render(request, 'slist.html',dict)

def addsub(request):
    if request.method=='POST':
        d=request.POST
        n=d['u']
        Subject.objects.create(title=n)
        return redirect('slist')
    return render(request,'Addsub.html')

def courses(request,sid):
    d=Course.objects.filter(subject=sid)
    sub=Subject.objects.get(id=sid)
    dict={'co':d,'sid':sid,'sub':sub}
    return render(request,'clist.html',dict)

def addcourse(request,sid):
    if request.method=='POST':
        d=request.POST
        na=d['u']
        ov=d['o']
        u=request.user.username
        user=User.objects.get(username=u)
        sub=Subject.objects.get(id=sid)
        Course.objects.create(owner=user,subject=sub,title=na,overview=ov)
        return redirect('slist')
    return render(request,'Addcourse.html')

def modules(request,cid):
    d=Module.objects.filter(course=cid)
    cou=Course.objects.get(id=cid)
    dict={'mo':d,'cid':cid,'cou':cou}
    return render(request,'mlist.html',dict)

def addmodule(request,cid):
    if request.method=='POST':
        d=request.POST
        na=d['u']
        ov=d['o']
        i=request.FILES['i']
        co=Course.objects.get(id=cid)
        Module.objects.create(course=co,title=na,description=ov,image=i)
        return redirect('slist')
    return render(request,'Addmodule.html')

def mdetail(request,mid):
    d=Module.objects.get(id=mid)
    di={'obj':d}
    return render(request,'Mdetail.html',di)