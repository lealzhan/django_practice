"""ch3_view_url URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from ch3_view_url.views import hello
from ch3_view_url.views import deardear
from ch3_view_url.views import doudou
from ch3_view_url.views import long_html
from ch3_view_url.views import template_test
from ch3_view_url.views import template_test_1
from ch3_view_url.views import template_test_2
from ch3_view_url.views import template_test_3



urlpatterns = [
               #url(r'', hello),                                 #default
               url(r'^admin/', include(admin.site.urls)),
               url(r'^hello/$', hello),
               url(r'^dear/$', deardear),
               url(r'^dou/$', doudou),
               url(r'^html/$', long_html),
               url(r'^template/$', template_test),
               url(r'^template1/$', template_test_1),
               url(r'^template2/$', template_test_2),
               url(r'^template3/$', template_test_3),
]
