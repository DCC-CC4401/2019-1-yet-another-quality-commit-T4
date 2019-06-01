from django.shortcuts import render

# Create your views here.

def landingpage(request):
    return render(request, 'Evaluador_interface/Landing_page_evaluador.html')
