from django.shortcuts import render
from .models import Flight, Airport
from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse('')