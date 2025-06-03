from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from appoint_forms.models import form_data
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt

def form(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        phone = request.POST.get('phone')
        tokenNo = request.POST.get('tokenNo')
        age = request.POST.get('age')
        diseaseInfo = request.POST.get('diseaseInfo')
        
        # Convert birthdate to a datetime.date object
    
        # Create and save the form instance
        form_instance = form_data(firstname=firstname,
                             lastname=lastname,
                             phone=phone,
                             tokenNo=tokenNo,
                             age=age,
                             diseaseInfo=diseaseInfo,
                             date=datetime.now()
                             )
        form_instance.save()
        
        return HttpResponse("Form submitted successfully.")
    else:
        return render(request, 'appointment.html')
