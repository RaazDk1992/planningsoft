from unicodedata import name
from django.conf.urls import handler404, handler500
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.default, name="default"),
    path('validate', views.verification, name='validate'),
    path('reg/',views.registerPlan,name="registerplan"),
    path('addfy/',views.addFY,name='addFy'),
    path('addprojecttype/',views.addProjectType,name='projecttype'),
    path('projectcategory/',views.addTypeOfProject,name='TypeOfProject'),
    path('admindashboard/',views.adminDashBoard,name='admindashboard'),
    path('adduser/',views.addStaff,name="adduser"),
    path('addoffice/',views.addOffice,name="addoffice")
]
