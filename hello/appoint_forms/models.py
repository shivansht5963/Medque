from django.db import models
from datetime import  datetime

class form_data(models.Model):
    firstname = models.CharField(max_length=100,  null=True)
    lastname = models.CharField(max_length=100,null=True)
    phone = models.IntegerField(null=True, blank=True)
    tokenNo = models.IntegerField(primary_key=True)
    age = models.IntegerField(null=True, blank=True)
    diseaseInfo = models.TextField()
    date = models.DateTimeField()
    
    def __str__(self):
        return self.firstname
   
