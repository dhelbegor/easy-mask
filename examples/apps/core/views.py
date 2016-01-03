from django.shortcuts import render
from django.views.generic import ListView
from .models import PersonalData




class ListView(ListView):
    template_name = 'index.html'
    context_object_name = 'personal'
    model = PersonalData
