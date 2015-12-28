"""ch5_model URL Configuration

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
from books.views import books_hello
from books.views import books_write
from books.views import books_read
from books.views import books_update
from books.views import image
from books.views import template
from books.views import bootstrap
from books.views import bootstrap_home
from books.views import bootstrap_feature
from books.views import bootstrap_contact
from books.views import form
from books.views import add
from books.views import index
from books.views import display_meta

urlpatterns = [
               url(r'^admin/', include(admin.site.urls)),
               url(r'^books/', books_hello),
               url(r'^bookswrite/', books_write),
               url(r'^booksread/', books_read),
               url(r'^booksupdate/', books_update),
               url(r'^image/', image),
               url(r'^template/', template),
               url(r'^bootstrap/', bootstrap),
               url(r'^bootstrap_home/', bootstrap_home),
               url(r'^bootstrap_feature/', bootstrap_feature),
               url(r'^bootstrap_contact/', bootstrap_contact),
               url(r'^form/', form),
               url(r'^add/', add),
               url(r'^index/', index),
               url(r'^display_meta/', display_meta),
]
