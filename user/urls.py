
from __future__ import absolute_import, unicode_literals


from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls import url, include
from . import views




urlpatterns = [
    path('',views.index,name='index'),
    path('contactus/',views.contactus,name='contactus'),
    path('sector/',views.sector,name='sector'),
    path('location/',views.location,name='location'),
    #path('login/',views.login,name='login'),
    #path('signup/',views.signup,name='signup'),
    path('search', views.search, name='search'),
    path('khulna/', views.khulna, name='khulna'),
    path('profile/<int:id>/', views.profile, name='profile'),
    path('othersprofile/<id>/', views.othersprofile, name='othersprofile'),



    path("chatroom/<int:pk>/", views.chatroom, name="chatroom"),
    path("ajax/<int:pk>/", views.ajax_load_messages, name="chatroom-ajax"),
    
]


