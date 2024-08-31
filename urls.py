# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('simulate/', views.simulate_surgery, name='simulate'),
    path('statistics/', views.view_statistics, name='statistics'),
]

# views.py
from django.shortcuts import render
from .models import Surgery, Patient, Outcome
import random

def simulate_surgery(request):
    # ... (logic for simulating surgery)
    return render(request, 'surgery_result.html', {'result': result})

# models.py
from django.db import models

class Surgery(models.Model):
    name = models.CharField(max_length=100)
    success_rate = models.FloatField()
    # ... other fields

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    # ... other fields

class Outcome(models.Model):
    surgery = models.ForeignKey(Surgery, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    result = models.CharField(max_length=20)
