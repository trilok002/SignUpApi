from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def home(request):
    return render(request,'home.html')

def All(request):
    data=Pizza.objects.all()
    z={'data':data}
    return render(request,'stored.html',z)

def add(request):
    if request.method=='POST':
        d=request.POST
        Pizza.objects.create(type=d['type'],size=d['size'],toppings=','.join(d.getlist('t1')))
        return redirect('home')
    return render(request,'add.html')

def delete(request,pid):
    d=Pizza.objects.get(id=pid)
    d.delete()
    return redirect('stored')

def edit(request,pid):
    p = Pizza.objects.get(id=pid)
    if request.method=="POST":
        d=request.POST
        p.type=d['type']
        p.size=d['size']
        p.toppings=','.join(d.getlist('t1'))
        p.save()
        return redirect('stored')
    d={'data':p}
    return render(request,'edit.html',d)

def sfilter(request,size):
    data=Pizza.objects.filter(size=size)
    d={'data':data,'size':size}
    return render(request,'filtered.html',d)


