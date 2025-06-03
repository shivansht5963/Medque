# urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Map the URL to the view
    path('', views.patient_list_view, name='patient_list_view'),
]
