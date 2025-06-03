from django.shortcuts import render
from .models import Patient
from datetime import datetime

def patient_list_view(request):
    patients = Patient.objects.all()
    return render(request, 'doctor.html', {'patients': patients})

