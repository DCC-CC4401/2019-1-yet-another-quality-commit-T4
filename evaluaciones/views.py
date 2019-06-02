from django.shortcuts import render
import json
from rubricas.processor import readCSV as reader
from rubricas.models import Rubrica as R
# Create your views here.
def evaluacion(request):
    name="prueba2"
    r = R.objects.filter(nombre=name).first()
    data = reader(r)
    header = reader(r)[0]
    data.pop(0)
    ll = [["Aspecto","hola","hola"],["Aspecto","hola","hola"],["Aspecto","hola","hola"],]
    data = json.dumps(data)
    header = json.dumps(header)
    return render(request, 'Eval_interface/evaluacion.html', context={'data':data,'header':header})

def evadmin(request):
    return render(request, 'Eval_interface/ficha_evaluacion.html')

def evmobile(request):
    return render(request, 'Eval_interface/evaluacionMobile.html')

def postev(request):
    return render(request, 'Eval_interface/postevaluacion.html')

def postevadmin(request):
    return render(request, 'Eval_interface/postevaluacionadmin.html')

