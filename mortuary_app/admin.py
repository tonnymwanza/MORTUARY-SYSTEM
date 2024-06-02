from django.contrib import admin

from . models import Appointment
# Register your models here.

@admin.register(Appointment)
class AdminAppointment(admin.ModelAdmin):
    list_display = [
        'name',
        'email',
        'phone_number',
        'appointment_date',
        'message',
        'id_number',
        'age_of_deceased',
        'relationship',
        'created',
        'appointment_status'
    ]

