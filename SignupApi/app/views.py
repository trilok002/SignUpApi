from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request):
    flag=False
    d={'flag':flag,'msg':'Incorrect Username or Password'}
    if request.method=='POST':
        dd=request.POST
        username=dd['user']
        password=dd['pass']
        user= authenticate(username=username,password=password)
        if user:
            login(request,user)
            if user.is_superuser:  ######### a super user can add and see the list of all Users.
                all_user=Users.objects.all()
                di={'user':user,'list':True,'auser':all_user,'cat':'All Users','desig':'Superuser'}

            else:
                u=Users.objects.get(user=user)
                if u.is_teacher:                 ####### a Teacher can add/list only the students
                    all_students=Users.objects.filter(is_teacher=False)  ### Filtering only student users
                    di={'user':user,'list':True,'auser':all_students,'cat':'All Students','desig':'Teacher'}
                else:
                    di={'user':user,'list':False,'desig':'Student'}  #######  a student can see only his information.
            return render(request,'userpage.html',di)
        else:
            flag=True
            d = {'flag': flag, 'msg': 'Incorrect Username or Password'}

    return render(request,'home.html',d)

def signup(request):
    flag=False
    d={'flag':flag,'msg':'Already registerd'}
    if request.method=='POST':
        dd=request.POST
        u=dd['user']
        f=dd['fn'].upper()
        l=dd['ln'].upper()
        e=dd['em']
        p=dd['pass']
        cp=dd['cpass']
        ra= True if(dd['r']=='Teacher') else False  # taking boolean input to check user is teacher or not
        if cp!=p:
            flag=True
            d = {'flag': flag, 'msg': 'Password mismatch'}
            return render(request, 'signup.html', d)
        try:
            user=User.objects.create_user(username=u,first_name=f,last_name=l,email=e,password=p)
            Users.objects.create(user=user,is_teacher=ra)
            return redirect('hm')
        except:
            flag = True
            d = {'flag': flag, 'msg': 'Already Registered'}


    return render(request,'signup.html',d)

def Logout(request):
    logout(request)
    return redirect('hm')

def add(request,cat): ##### to add user for superuser and teacher also, teacher can add only student
    check=False
    if cat=='All Users':
        flag=True
    else:
        flag=False
    d={'flag':flag}
    if request.method=='POST':
        dd = request.POST
        u = dd['user']
        f = dd['fn'].upper()
        l = dd['ln'].upper()
        e = dd['em']
        p = dd['pass']
        cp = dd['cpass']
        ra = True if (dd['r'] == 'Teacher') else False
        if cp != p:
            check = True
            d = {'check': check, 'msg': 'Password mismatch'}
            return render(request, 'add.html', d)
        try:
            user = User.objects.create_user(username=u, first_name=f, last_name=l, email=e, password=p)
            Users.objects.create(user=user, is_teacher=ra)
            print(request.is_authenticated())
            return redirect('hm')
        except:
            check = True
            d = {'check': check, 'msg': 'Already Registered'}

    return render(request,'add.html',d)

