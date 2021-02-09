from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path("",views.template1,name='home'),
    path("login/",views.template2,name='login'),
    path("education/",views.template3,name='education'),
    path("about/",views.template4,name='about'),
]