from django.shortcuts import render,redirect

from .models import *
# Create your views here.
def All_category():
    all_cat = Category.objects.all()
    return all_cat

def Recent_and_pop():
    allpost=Post.objects.all()
    rect=allpost[::-1][:3]
    like=[]
    le=len(allpost)
    newp=[]
    for i in allpost:
        l= likecomment.objects.filter(post_data=i,like=True).count()
        like.append(l)
    for i in range(le):
        if max(like)>0:
            m= max(like)
            p= like.index(m)
            po= allpost[p]

            like.pop(p)
            like.insert(p,0)
            newp.append(po)
    topt=newp[:3]
    return topt,rect


def home(request):
    all_post=Post.objects.all()
    li=[]
    for i in all_post:
        like = likecomment.objects.filter(post_data = i,like=True).count()
        li.append(like)
    z=zip(all_post,li)
    top3,rec3=Recent_and_pop()
    d = {"allcat":All_category(),"all_Post":z,'top3':top3,'rec3':rec3}
    return render(request,'index.html',d)

def about(request):
    d = {"allcat": All_category()}
    return render(request,'about.html',d)

from django.contrib.auth import authenticate,login,logout
def Login(request):
    error=False
    if request.method=="POST":
        d1=request.POST
        n= d1['ln']
        p= d1['ps']
        user = authenticate(username=n,password=p)
        if user:
            login(request,user)
        else:
            error=True
    d = {"allcat": All_category(),'error':error}
    return render(request,'login.html',d)

def signup(request):
    error=False

    if request.method == "POST":
        dd = request.POST
        n= dd['nm']
        u= dd['unm']
        e= dd['em']
        p= dd['ps']
        i= request.FILES['img']
        udata=User.objects.filter(username=u)
        if udata:
            error=True
        else:
            user = User.objects.create_user(username=u,password=p,first_name=n)
            userdetail.objects.create(user=user,image=i)
            return redirect('lg')
    d = {"allcat": All_category(),'error':error}
    return render(request,'signup.html',d)

def contact(request):
    d = {"allcat": All_category()}
    return render(request,'contact.html',d)

def blogdetail(request,bid):
    detail= Post.objects.get(id=bid)

    d= {'detail':detail}
    return render(request,'singlepage.html',d)

def like_post(request,pid):
    if not request.user.is_authenticated:
        return redirect('lg')
    data = Post.objects.get(id=pid)
    data2 = likecomment.objects.filter(post_data=data,usr=request.user,like=True)

    if not data2:
        data3=likecomment.objects.filter(post_data=data,usr=request.user).first()
        if data3:
            data3.like=True
            data3.save()
        else:
            likecomment.objects.create(post_data=data, usr=request.user, like=True)
            return redirect('hm')
    else:
        return redirect('hm')


def Logout(request):
    logout(request)
    return redirect('lg')

from datetime import date
def Post_comment(request,pid):
    if not request.user.is_authenticated:
        return redirect('lg')
    pdata=Post.objects.get(id=pid)
    user = request.user
    td= date.today()

    if request.method=='POST':
        d=request.POST
        c= d['Message']
        data =likecomment.objects.filter(usr=request.user,post_data=pdata).first()
        if data:
            data.comment=c
            data.save()
        else:
            likecomment.objects.create(usr=user, post_data=pdata, comment=c, date=td)
    return redirect('Bde',pid)

def myblog(request):
    data=Post.objects.filter(user=request.user)
    d={'data':data,"allcat": All_category()}
    return render(request,'fashion.html',d)

def blogdelete(request,bid):
    data= Post.objects.get(id=bid)
    data.delete()
    return redirect('mb')

def catdetail(request,cid):
    cdata=Category.objects.get(id=cid)
    d={'cdata':cdata}
    return render(request,'detail.html',d)


from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.conf import settings

def Addblog(request):
    if request.method=="POST":
        dd=request.POST
        t=dd['title']
        s=dd['sde']
        l=dd['lde']
        cat=dd['cat']
        image=request.FILES['img']
        cdata=Category.objects.get(id=cat)
        user=request.user
        td=date.today()
        Post.objects.create(cat=cdata,user=user,title=t,short_des=s,long_des=l,image=image,date=td)



        return redirect('mb')
    d = { "allcat": All_category()}
    return render(request,'addblog.html',d)

def changeimage(request):
    udata = userdetail.objects.filter(user=request.user).first()
    if request.method=="POST":

        i=request.FILES['img']
        udata.image=i
        udata.save()
        return redirect('mb')
    d={'udata':udata}
    return render(request,'changei.html',d)

def changepass(request):
    error=False
    if request.method=="POST":
        dd=request.POST
        o=dd['old']
        n=dd['new']
        data=authenticate(username=request.user.username,password=o)
        if data:
            data.set_password(n)
            data.save()
            logout(request)
            login(request,data)
            return redirect('mb')
        else:
            error=True
    d={'error':error}
    return render(request,'changep.html',d)

