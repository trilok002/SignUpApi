"""educa URL Configuration

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
from courses.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Login,name='login'),
    path('sublist',subjects,name='slist'),
    path('addsub',addsub,name='addsub'),
    path('couses/<int:sid>',courses,name='courses'),
    path('addcorse/<int:sid>',addcourse,name='addcourse'),
    path('modulelist/<int:cid>',modules,name='modules'),
    path('addmodule/<int:cid>',addmodule,name='addmo'),
    path('mdetail/<int:mid>',mdetail,name='mdetail')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
