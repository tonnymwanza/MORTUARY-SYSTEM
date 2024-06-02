from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages

from . forms import AppointmentForm
from . models import Appointment
# Create your views here.

class HomeView(View):
    
    def get(self, request):
        return render(request, 'index.html')
    
def register(request):
    if request.method  == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'the username is use. find another one')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'the email is in use. find another one')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                return redirect('signin')
        else:
            messages.error(request, 'the passwords dont match. Repeat')
            # return redirect('register')
    return render(request, 'signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST['next'])
            else:
                return redirect('home')
        else:
            messages.error(request, 'incorrect username or password')
            return redirect('signin')
    return render(request, 'signup.html')

class AppointmentView(View):

    def get(self, request):
        form = AppointmentForm()
        context = {
            'form': form
        }
        return render(request, 'appointment.html', context)
    
    def post(self, request):
        form = AppointmentForm(request.POST or None)
        if form.is_valid():
            appointment = Appointment.objects.create(
                user = request.user,
                name = form.cleaned_data['name'],
                email =form.cleaned_data['email'],
                phone_number = form.cleaned_data['phone_number'],
                appointment_date = form.cleaned_data['appointment_date'],
                id_number = form.cleaned_data['id_number'],
                age_of_deceased = form.cleaned_data['age_of_deceased'],
                relationship = form.cleaned_data['relationship'],
                message = form.cleaned_data['message']
            )
            form = AppointmentForm()
            messages.info(request, 'Thankyou for booking the appointment.')
        else:
            messages.error(request, 'Error booking appointment')
        return redirect('appointment')
    
class TrackingView(View):

    def get(self, request):
        appointment_list = Appointment.objects.all()
        context= {
            'appointment_list': appointment_list
        }
        return render(request, 'tracking.html', context)
    