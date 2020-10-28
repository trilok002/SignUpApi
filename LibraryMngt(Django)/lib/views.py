from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .models import *

# Create your views here.
def Home(req):
    data=Books.objects.all()
    l=len(data)-4
    lat=data[:l:-1]
    d={'data':lat}
    return render(req, 'index.html',d)

def Login(request):
    dict={'flag':False,'msg':''}
    if request.method=="POST":
        d=request.POST
        user=d['user']
        pas= d['pass']
        if len(user)==12:
            user=user.upper()
        userdata=authenticate(username=user,password=pas)

        if userdata:
            if userdata.is_superuser:
                return redirect('adbooks')

            elif Students.objects.filter(enroll=user):

                if authenticate(username=user, password=pas):
                    login(request, authenticate(username=user, password=pas))
                    return redirect('stdpage')
            else :
                return HttpResponse(request,'something went wrong')

        else:
            dict = {'flag': True, 'msg': '* incorrect username or password.'}
            return render(request, 'Login.html',dict)

    return render(request, 'Login.html',dict)

def Register(request):
    dict={'flag':False,'msg':''}
    if request.method=="POST":
        d=request.POST
        p=d['pass']
        c=d['cpass']
        mo=d['mo']
        en=d['en'].upper()
        na=d['na'].upper()
        email=d['email']
        br=d['br'].upper()
        col=d['co'].upper()
        if Students.objects.filter(enroll=en):
            dict = {'flag': True, 'msg': '* Already registered .'}
            return render(request, 'Register.html', dict)
        if len(en)!=12:
            dict = {'flag': True, 'msg': '* incorrect enrollment .'}
            return render(request, 'Register.html', dict)
        if len(mo)!=10:
            dict = {'flag': True, 'msg': '* incorrect mobile no.'}
            return render(request, 'Register.html', dict)
        if c!=p:
            dict={'flag':True,'msg':'**incorrect password'}
            return render(request,'Register.html',dict)
        Students.objects.create(enroll=en,name=na,branch=br,college=col,mobile=mo,email=email,password=p)
        User.objects.create_user(username=en,password=p)
        return redirect('home')
    return render(request,'Register.html',dict)

def MyBooks(request):
    data=Books.objects.all()
    d={'data':data}
    return render(request, 'Books.html',d)

def InsertBook(request):
    if request.method=='POST':
        d=request.POST
        n=d['book'].upper()
        a=d['auth'].upper()
        b=d['gen'].upper()
        i=request.FILES['bimage']
        det=d['det']
        Books.objects.create(bname=n,bauthor=a,genres=b,bimage=i,bdetail=det)
        return redirect('adbooks')
    return render(request,'InsertBook.html')

def removebook(request,bid):
    Books.objects.filter(id=bid).delete()
    return redirect('adbooks')



def selected(request,str,i):

    data=Books.objects.filter(genres=str)
    d={'data':data,'str':str,'int':i}
    return render(request, 'Selected.html',d)

def stdapply(request,i,bid):

    if i=='0':
        return redirect('login')

    else:
        print(i,bid)
        book=Books.objects.get(id=bid)
        d={'book':book,'enroll':i}
        return render(request,'Applybook.html',d)

def Logout(request):
    logout(request)
    return redirect('home')

def stdpage(request):
    user=request.user.username
    obj = Brecord.objects.filter(stdenroll=user)
    list = []
    ob = Students.objects.filter(enroll=user)
    for i in obj:
        list.append(Books.objects.get(id=i.apbid))

    z = zip(list, obj)
    d = {'obj': ob[0], 'data': z}
    return render(request, 'StdPage.html', d)


def applyRecord(request,en,bid):
    if request.user.is_authenticated and bid is not None:
        print(en, bid)

        Brecord.objects.create(stdenroll=en,apbid=bid,issued=False)
        return redirect('stdpage')

    else:
        return redirect('login')

def search(req):
    if req.method=='POST':
        d=req.POST
        name=d['search'].upper()
        book=Books.objects.filter(bname=name)
        if book:
            if req.user.is_authenticated:
                en=req.user.username
            else:en='0'
            d = {'book': book[0], 'enroll': en}
            return render(req, 'Applybook.html', d)

        else:
            return HttpResponse('no match found')
    return HttpResponse('something went wrong')