from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def landingpage(request):
    return render(request, 'Admin_interface/Landing_page_admin.html')

def rubricas(request):
    return render(request, 'Admin_interface/Rubricas_admin.html')

def evaluaciones(request):
    return render(request, 'Admin_interface/Evaluaciones_admin.html')