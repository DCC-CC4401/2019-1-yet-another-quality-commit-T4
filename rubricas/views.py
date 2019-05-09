from django.shortcuts import render

# Create your views here.
def rubadmin(request):
    return render(request, 'Admin_interface/Rubricas_admin.html')

def fichaadmin(request):
    return render(request, 'FichasRubricas/FichaRubricaAdministrador.html')

def fichaeval(request):
    return render(request, 'FichasRubricas/FichaRubricaEvaluador.html')

