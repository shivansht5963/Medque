# doctor/templatetags/patient_tags.py
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def render_patient_details(patient):
    # Check if patient is an object with attributes
    if hasattr(patient, 'firstname'):
        # Construct HTML safely
        return mark_safe(f"""
            <p>First Name: {patient.firstname}</p>
            <p>Last Name: {patient.lastname}</p>
            <p>Phone: {patient.phone}</p>
            <p>Token No: {patient.tokenNo}</p>
            <p>Age: {patient.age}</p>
            <p>Disease Info: {patient.diseaseInfo}</p>
        """)
    else:
        return "Invalid patient data"
