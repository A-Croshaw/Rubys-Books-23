from django.urls import path
from . import views

urlpatterns = [
     path('contact/',views.contact,name='contact'),
     path('thank_you/',views.thank_you,name='thank_you'),
]