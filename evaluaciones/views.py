from django.shortcuts import render
import json

from evaluaciones.models import Evaluacion
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

def evadmin(request, evaluacion_id):
    print(evaluacion_id)
    eval = Evaluacion.objects.get(id=evaluacion_id)
    return render(
        request,
        'Eval_interface/ficha_evaluacion.html',
        context={
            "evaluacion": eval,
            "evaluadores": eval.evaluadores.all(),
            "equipos": eval.curso.equipos.all(),
            "integrantes": {
                equipo.nombre: equipo.estudiantes.all()
                for equipo in eval.curso.equipos.all()
            }
        }
    )

def evmobile(request):
    return render(request, 'Eval_interface/evaluacionMobile.html')

def postev(request):
    return render(request, 'Eval_interface/postevaluacion.html')

def postevadmin(request):
    return render(request, 'Eval_interface/postevaluacionadmin.html')

