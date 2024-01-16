from django.db import models

class Contact(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    message=models.TextField()

class Schemesinfo(models.Model):
    schemename =models.CharField(max_length=50)
    citizensip =models.CharField(max_length=50)
    State =models.CharField(max_length=50)
    age =models.CharField(max_length=50)    
    gender =models.CharField(max_length=50)    
    caste =models.CharField(max_length=50)    
    rationcard =models.CharField(max_length=50)
    employmentStatus =models.CharField(max_length=50)
    aadhaarnumber =models.CharField(max_length=12)    
    link=models.URLField()

class Applications(models.Model):
    first_name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    citizensip = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    caste = models.CharField(max_length=20)
    rationcard = models.CharField(max_length=20)
    employmentStatus = models.CharField(max_length=50)
    aadhaarnumber = models.CharField(max_length=50)
    schemename = models.CharField(max_length=50)
    is_approved = models.BooleanField(default=False)



# Create your models here.
