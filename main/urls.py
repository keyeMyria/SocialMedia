"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url , include
from django.urls import path
from django.contrib import admin
from scrp.views import *
from django.conf import settings
from django.conf.urls.static import static

from gallery.views import (serve_gallery , serve_gallery_all, test_1)
from chatroom.views import *
from ipack import tags


urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'',main,name="login page and home"),
    path(r'prof',prof,name="profile"),
    path(r'sign',sign,name="sing in "),
    path(r'captcha/', include('captcha.urls')),
    path(r'accounts/',include('registration.backends.default.urls')),
    path(r'mobile/',include('mob.urls')),
    path(r'pattern/',include('scrp.url')),
    path(r'inner/',include('inner.urls')),
    path(r'jobs/', include('fetcher.urls')),
    #url(r'^asyn/',list_d),
    path(r'settings',setup),
    path(r'gallery',serve_gallery,name="img gallery of serving"),
    path(r'gallery/all',serve_gallery_all,name="img gallery of all images"),
    #url(r'^gallery/l$',test_1),
    path(r'ws/', include("chatroom.urls")),
    path(r'friends/', include("friends.urls")),
    
]
if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

tags.boot()







