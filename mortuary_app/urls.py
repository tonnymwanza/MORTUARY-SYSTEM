from django.urls import path

from . import views
from . views import HomeView
from . views import AppointmentView
from . views import TrackingView
# my urls

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('register', views.register, name='register'),
    path('signin', views.signin, name='signin'),
    path('appointment', AppointmentView.as_view(), name='appointment'),
    path('tracking', TrackingView.as_view(), name='tracking'),
]