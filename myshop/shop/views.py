from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def myshop(request):
    data=Category.objects.all()
    d={'data':data}
    return render(request,'Myshop.html',d)

def products(request,cid):
    ow=Category.objects.get(id=cid)
    data=Product.objects.filter(category=ow)

    d={'data':data,'cat':ow.name}
    return render(request,'Products.html',d)

def addtocart(request,pid):
    p=Product.objects.get(id=pid)
    Cart.objects.create(products=p)
    return redirect('your')

def yourcart(request):
    data = Cart.objects.all()
    li = []
    for i in data:
        li.append(Product.objects.get(name=i))
    z=zip(li,data)
    d={'data':z}
    return render(request, 'Cart.html',d)

