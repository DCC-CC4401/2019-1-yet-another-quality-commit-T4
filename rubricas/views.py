from django.shortcuts import render, redirect
from django.http import HttpResponse
from rubricas.models import Rubrica as R
from rubricas.processor import make as makeRubric
# Create your views here.

def rubadmin(request):
    return render(request, 'Admin_interface/Rubricas_admin.html',{
        # 'miau':['rubrica1','rubrica2','rubrica3'], # Dummy data
        'rubs': R.objects.order_by('-id')[:5], # show the latest 5 records in Rubrica
    }
)

def fichaadmin(request):
    return render(request, 'FichasRubricas/FichaRubricaAdministrador.html')

def fichaeval(request):
    return render(request, 'FichasRubricas/FichaRubricaEvaluador.html')

def data(request):

    p = request.POST
    makeRubric(p)
    return redirect('../a')

def deleterubric(request):
    p = request.POST
    print(p)
    id = int(p['obj_id'])
    R.objects.filter(id=id).delete()
    return redirect('/rub/a')