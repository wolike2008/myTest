"""myTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from myblog import views,api

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('',views.index),
    path('classes/',views.classes),

    #api接口
    path('api/',api.api_test),
    path('get-menu-list/',api.getMenuList),
    path('get-user-list/',api.getUserList),
    path('login/',api.toLogin),
    path('register/',api.toRegister),
    path('upload-logo/',api.uploadLogo)
] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)\
    + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
