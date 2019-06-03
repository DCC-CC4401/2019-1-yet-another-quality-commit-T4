from django.shortcuts import render, redirect
import json

from evaluaciones.models import Evaluacion
from rubricas.processor import readCSV as reader
from django.http import HttpResponse

from rubricas.models import Rubrica as R
from cursos.models import Equipo, Estudiante, Curso
from evaluaciones.models import Evaluacion, EvaluacionGrupo, Resultados
from usuarios.models import Evaluador
import time

# Create your views here.
def evaluacion(request, evaluacion_id, equipo_id, estudiante_id):
    print(evaluacion_id, equipo_id, estudiante_id)
    evaluacion = Evaluacion.objects.get(id=evaluacion_id)
    r = evaluacion.rubrica
    estudiante = Estudiante.objects.get(id=estudiante_id)
    equipo = Equipo.objects.get(id=equipo_id)
    d_user = request.user
    evaluador = Evaluador.objects.get(user=d_user)
    print(evaluador.email)
    curso = evaluacion.curso

    print(evaluacion, r, estudiante, equipo, evaluador)

    data = reader(r)
    header = reader(r)[0]
    data.pop(0)
    data = json.dumps(data)
    header = json.dumps(header)

    return render(request, 'Eval_interface/evaluacion.html',
                  context={'data' : data,
                           'header' : header,
                           'grupo' : equipo,
                           'estudiante' : estudiante,
                           'evaluador' : evaluador,
                           'curso' : curso,
                            'evaluacion' : evaluacion}
                  )
def postevresult(request):
    p = request.POST


    grupo=Equipo.objects.filter(id=p['grupo']).get()
    presentador = Estudiante.objects.filter(id=p['presentador']).get()
    evaluacion = Evaluacion.objects.filter(id=p['evaluacion']).get()
    hoy = time.strftime('%Y-%m-%d')
    evGrupo = EvaluacionGrupo.objects.create(
        grupo=grupo,
        presentador=presentador,
        evaluacion=evaluacion,
        fecha=hoy)
    pje = p['puntaje']
    evaluador = Evaluador.objects.filter(id=p['evaluador']).get()

    result = Resultados.objects.create(
        evaluador=evaluador,
        puntaje=pje,
        evaluacion_grupo=evGrupo
    )

    print(p['evaluador'])
    return redirect('/a/eval/')


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

def evaluacion_admin(request):
    return render(request, 'Eval_interface/evaluacionadmin.html')