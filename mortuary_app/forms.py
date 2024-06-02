from django import forms

from . models import Appointment
# create your forms here

class AppointmentForm(forms.Form):
    relationship_choices = (
        ('mother', 'Mother'),
        ('father', 'Father'),
        ('sister', 'Sister'),
        ('brother', 'Brother'),
        ('other', 'Other')
    )
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name of the deceased'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Enter your email',}))
    phone_number = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Enter your phone number'}))
    appointment_date = forms.DateField(widget=forms.DateInput({'placeholder': 'Pick date', 'type': 'date'}))
    id_number = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'id number of the deceased if available'}))
    age_of_deceased = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'The age of the deceased'}))
    relationship = forms.CharField(widget=forms.Select(attrs={'placeholder': 'Your relationship with the deceased'}, choices=relationship_choices))
    message = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your message', 'rows': 10}))