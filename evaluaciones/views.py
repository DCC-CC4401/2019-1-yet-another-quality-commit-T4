from django.shortcuts import render
import json
# Create your views here.
def evaluacion(request):
    ll = [["Aspecto","hola","hola"],["Aspecto2", "chao", "chao"]]
    data = json.dumps(ll)
    return render(request, 'Eval_interface/evaluacion.html', context={'data':data})

def evadmin(request):
    return render(request, 'Eval_interface/ficha_evaluacion.html')

def evmobile(request):
    return render(request, 'Eval_interface/evaluacionMobile.html')

def postev(request):
    return render(request, 'Eval_interface/postevaluacion.html')

def postevadmin(request):
    return render(request, 'Eval_interface/postevaluacionadmin.html')

