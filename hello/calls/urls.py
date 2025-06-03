from django.urls import path
from .views import exotel_webhook

urlpatterns = [
    path('', exotel_webhook, name='exotel_webhook'),
]
