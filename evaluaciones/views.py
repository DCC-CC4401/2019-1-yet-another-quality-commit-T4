from django.shortcuts import render, redirect
import json
from rubricas.processor import readCSV as reader
from django.http import HttpResponse

from rubricas.models import Rubrica as R
from cursos.models import Equipo, Estudiante, Curso
from evaluaciones.models import Evaluacion, EvaluacionGrupo, Resultados
from usuarios.models import Evaluador
import time

# Create your views here.
def evaluacion(request):

    if request.method=='POST':
        evaluacion = Evaluacion.objects.filter(id=request.POST['idEvaluacion'])
        presentador = Estudiante.objects.filter(id=request.POST['idPresentador'])
        equipo = Equipo.objects.filter(id=request.POST['idEquipo'])
        evaluador = Evaluador.objects.filter(id=request.POST['idEvaluador'])
    name = "prueba3"
    r = R.objects.filter(nombre=name).get()
    estudiante = Estudiante.objects.filter(nombre="1").get()
    grupo = Equipo.objects.filter(nombre="Equipo1").get()
    evaluador = Evaluador.objects.filter(nombre='luis').first()
    print(evaluador.email)
    curso = Curso.objects.filter(nombre='curso').get()
    evaluacion = Evaluacion.objects.filter(nombre='Evaluacion').first()

    data = reader(r)
    header = reader(r)[0]
    data.pop(0)
    data = json.dumps(data)
    header = json.dumps(header)

    return render(request, 'Eval_interface/evaluacion.html',
                  context={'data':data,
                           'header':header,
                           'grupo':grupo,
                           'estudiante':estudiante,
                           'evaluador':evaluador,
                           'curso':curso,
                            'evaluacion':evaluacion}
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


def evadmin(request):
    return render(request, 'Eval_interface/ficha_evaluacion.html')

def evmobile(request):
    return render(request, 'Eval_interface/evaluacionMobile.html')

def postev(request):
    return render(request, 'Eval_interface/postevaluacion.html')

def postevadmin(request):
    return render(request, 'Eval_interface/postevaluacionadmin.html')

def evaluacion_admin(request):
    return render(request, 'Eval_interface/evaluacionadmin.html')