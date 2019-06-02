from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from evaluaciones.models import Evaluacion
from usuarios.models import Evaluador
from cursos.models import Curso
from rubricas.models import Rubrica

# Create your views here.
def landingpage(request):
    return render(request, 'Admin_interface/Landing_page_admin.html')

def rubricas(request):
    return render(request, 'Admin_interface/Rubricas_admin.html')

def evaluaciones(request):
    evaluaciones_ = Evaluacion.objects.all()
    evaluadores = Evaluador.objects.all()
    cursos = Curso.objects.all()
    rubricas = Rubrica.objects.all()
    return render(request, 'Admin_interface/Evaluaciones_admin.html', context={'evaluaciones': evaluaciones_, 'evaluadores': evaluadores, 'cursos': cursos, 'rubricas': rubricas})

def deleteEvaluacion(request):

    delete=request.POST.get('id_evaluacion')
    Evaluacion.objects.filter(id=delete).delete()
    return redirect('/a/eval/')


def modifyEvaluacion(request):
    nombre = request.POST.get('nombre')
    curso = Curso.objects.filter(id=request.POST.get('curso')).get()
    fecha_ini = request.POST.get('fecha_ini')
    fecha_fin = request.POST.get('fecha_fin')
    evaluadores = request.POST.getlist('evals')
    evaluacion = Evaluacion.objects.filter(id=request.POST.get('evaluacion')).get();
    rubrica = Rubrica.objects.filter(id=request.POST.get('rubrica')).get()
    evaluacion.evaluadores.through.objects.all().delete();
    evaluacion.nombre=nombre
    evaluacion.curso=curso
    evaluacion.rubrica=rubrica
    evaluacion.fecha_inicio = fecha_ini
    evaluacion.fecha_fin = fecha_fin
    for eva in evaluadores:
        evaluacion.evaluadores.add(
            Evaluador.objects.get(
                user=User.objects.get(username=eva)
            )
        )
    evaluacion.save()


    return redirect('/a/eval/')

def createEvaluacion(request):
 #   # TODO: poner la llave real de curso y rubrica
    if request.method == 'POST':
        print('se viene el POST!!: ', request.POST)
        evaluadores = request.POST.getlist('evals')
        fecha_ini = request.POST.get('fecha_ini')
        fecha_fin = request.POST.get('fecha_fin')
        rub = request.POST.get('rubrica')
        nombre = request.POST.get('nombre')
        print(type(request.POST.get('curso')))
        curso = Curso.objects.filter(nombre=request.POST.get('curso')).get()
        print(curso.id)
        rubrica = Rubrica.objects.filter(nombre=rub).get()
        evaluacion = Evaluacion.objects.create(
            nombre=nombre,
            fecha_inicio=fecha_ini,
            fecha_fin=fecha_fin,
            curso=curso,
            rubrica=rubrica,
        )
        evaluacion.save()
        for eva in evaluadores:
            evaluacion.evaluadores.add(
                Evaluador.objects.get(
                    user=User.objects.get(username=eva)
                )
            )
    print(evaluacion.fecha_inicio, evaluacion.fecha_fin, evaluacion.estado)
    return redirect('/a/eval/')
