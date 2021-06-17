from .views import login, register, index, myPosts, createPosts, follow, unfollow

from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^login/$', login, name='login'),
    url(r'^register/$', register, name='register'),

    url(r'^index/$', index, name='index'),
    
    url(r'^myPosts/$', myPosts, name='myPosts'),
    url(r'^createPosts/$', createPosts, name='createPosts'),
    
    url(r'^follow/$', follow, name='follow'),
    url(r'^unfollow/$', unfollow, name='unfollow'),
]