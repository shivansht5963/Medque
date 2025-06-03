from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Patient(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    tokenNo = models.CharField(max_length=20)
    age = models.IntegerField()
    diseaseInfo = models.TextField()

    def __str__(self):
        return self.name
