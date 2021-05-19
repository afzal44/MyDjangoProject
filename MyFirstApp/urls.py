from django.contrib import admin
from django.urls import path
from MyFirstApp import views
urlpatterns = [
    path('', views.index,name='home'),
    path('services', views.services,name='service'),
    path('contact', views.contacts,name='contact'),
    path('about', views.about,name='about')
]
