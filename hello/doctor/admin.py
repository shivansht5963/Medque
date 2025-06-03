# doctor/admin.py
from django.contrib import admin
from .models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'phone', 'tokenNo', 'age', 'diseaseInfo')
