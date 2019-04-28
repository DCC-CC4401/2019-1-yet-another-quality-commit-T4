from django.shortcuts import render

# Create your views here.
def curadmin(request):
    return render(request, 'Admin_interface/Cursos_admin.html')