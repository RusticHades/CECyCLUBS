from django.shortcuts import render

# Create your views here.
# inicio/views.py

from django.http import HttpResponse

def inicio(request):
    return render(request,'inicio.html')
