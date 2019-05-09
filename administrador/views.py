from django.shortcuts import render

# Create your views here.
def landingpage(request):
    return render(request, 'Admin_interface/Landing_page_admin.html')

def evaluadores(request):
    return render(request, 'Admin_interface/Evaluadores_admin.html')