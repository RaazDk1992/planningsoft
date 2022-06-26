from django.conf.urls import handler404, handler500
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.default, name="revhome"),
    path('reg/',views.registerPlan,name="registerplan")
]
