"""Blogger URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Blog.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='hm'),
    path('about/',about,name='ab'),
    path('login/',Login,name='lg'),
    path('signup/',signup,name='su'),
    path('contact/',contact,name='con'),
    path('blogdetail/<int:bid>/',blogdetail,name='Bde'),
    path('blog_like/<int:pid>',like_post,name='like'),
    path('logout/',Logout,name='logout'),
    path('blogcomment/<int:pid>/',Post_comment,name='postc'),
    path('myblog/',myblog,name='mb'),
    path('blogdelete/<int:bid>/',blogdelete,name='blgde'),
    path('catdetail/<int:cid>/',catdetail,name='cde'),
    path('addblog/',Addblog,name='adb'),
    path('changeimage/',changeimage,name='chi'),
    path('changepass/',changepass,name='chp'),
]+static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)
