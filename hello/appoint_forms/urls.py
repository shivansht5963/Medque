from django.contrib import admin
from django.urls import path
from appoint_forms import views

urlpatterns = [
    path('',views.form,name='form')
]
