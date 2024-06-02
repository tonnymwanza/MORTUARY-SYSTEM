from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.IntegerField()
    appointment_date = models.DateField() 
    appointment_status = models.CharField(max_length=50, null=True)
    message = models.TextField()
    id_number = models.IntegerField(null=True, blank=True)
    age_of_deceased = models.IntegerField(null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    relationship = models.CharField(max_length=50, null=True)
