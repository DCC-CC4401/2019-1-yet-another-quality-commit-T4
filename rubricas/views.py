from django.shortcuts import render, redirect
from django.http import HttpResponse
from rubricas.models import Rubrica as R
from rubricas.processor import make as makeRubric, readCSV
import json
import os
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

    r = R.objects.filter(id=id).first()
    file = r.get_path()
    os.remove(file)
    r.delete()

    return redirect('/rub/a')

def verrubrica(request):
    p=request.POST
    print(p)
    print("hola")
    id = int(p['obj_id'])
    r = R.objects.filter(id=id).first()
    min_duration = r.get_min_duration()
    max_duration = r.get_max_duration()
    cells = readCSV(r)
    rows = len(cells)
    colls = len(cells[0])
    print(cells)
    return render(request, 'FichasRubricas/FichaRubricaAdministrador.html',
                  {'rub': r,
                   'cells':cells,
                   'rows':rows,
                   'colls':colls,
                   'max_duration':max_duration,
                   'min_duration':min_duration,
                   'readonly':'readonly',
                   'data':json.dumps(cells),
                   }
                  )