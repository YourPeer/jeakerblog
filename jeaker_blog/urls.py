"""jeaker_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from myblog import views as view
from jeaker_blog.settings import MEDIA_ROOT
from django.views.static import serve
urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'about/', view.about),
    path(r'index/', view.index),
    path(r'say/', view.say),
    path(r'daynote/', view.daynote),
    path(r'photo/', view.photo),
    path(r'learn/', view.learn),
    path(r'guestbook/', view.guestbook),
    path(r'editor/', view.editor),
    path(r'blogpost/', view.blogpost),
    url(r'^blog/(\d+)/$',view.artical),
    url(r'^media/(?P<path>.*)$',  serve, {"document_root": MEDIA_ROOT}),
]
