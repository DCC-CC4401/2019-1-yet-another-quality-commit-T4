from django.shortcuts import render
from django.http import HttpResponse
from rubricas.models import Rubrica as R
import csv
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
    nombre = p['0,0']
    r = R(nombre=p['0,0'],durationMin=p['min_duration'],durationMax=p['max_duration'])
    r.save()
    with open('rubricas/storage/'+nombre+'.csv','w') as file:
        wr = csv.writer(file, quoting = csv.QUOTE_ALL)
        wr.writerow([p['0,0'],p['0,1'],p['0,2']])
    a=""
    for cell in p:
       a=a+" " +cell +" " +p[cell] + "\n"
    print(p)
    return rubadmin(request)