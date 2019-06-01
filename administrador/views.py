from django.shortcuts import render, redirect
from evaluaciones.models import Evaluador, Evaluacion
from cursos.models import Curso
from rubricas.models import Rubrica
from django.utils.crypto import get_random_string
import time

# Create your views here.
def landingpage(request):
    return render(request, 'Admin_interface/Landing_page_admin.html')

def evaluadores(request):
    if(request.method == 'POST'):
        name = request.POST.get('name')
        lname = request.POST.get('lname')
        mail = request.POST.get('mail')
        password = get_random_string(8)

        Evaluador.objects.create(
            nombre=name,
            apellido=lname,
            email=mail,
            contrasenna=password
        )

    evaluadores = Evaluador.objects.all()

    return render(request, 'Admin_interface/Evaluadores_admin.html', context={'evaluadores': evaluadores})

def deleteEvaluador(request):
    mail_to_delete = request.POST.get('evaluador')
    Evaluador.objects.filter(email = mail_to_delete).delete()
    return redirect('/a/ev/')

def modifyEvaluador(request):
    new_name = request.POST.get('new_name')
    new_lname = request.POST.get('new_lname')
    new_mail = request.POST.get('new_mail')
    previous_mail = request.POST.get('evaluador')


    modified = Evaluador.objects.get(email = previous_mail)
    if(new_name != ''):
        modified.nombre = new_name

    if(new_lname != ''):
        modified.apellido = new_lname

    if(new_mail != ''):
        modified.email = new_mail

    modified.save()
    return redirect('/a/ev/')

def rubricas(request):
    return render(request, 'Admin_interface/Rubricas_admin.html')

def evaluaciones(request):
    evaluaciones = Evaluacion.objects.all()
    evaluadores = Evaluador.objects.all()
    cursos = Curso.objects.all()
    rubricas = Rubrica.objects.all()
    return render(request, 'Admin_interface/Evaluaciones_admin.html', context={'evaluaciones': evaluaciones, 'evaluadores': evaluadores, 'cursos': cursos, 'rubricas': rubricas})

def deleteEvaluacion(request):

    delete=request.POST.get('id_evaluacion')
    Evaluacion.objects.filter(id=delete).delete()
    return redirect('/a/eval/')

def createEvaluacion(request):
 #   # TODO: poner la llave real de curso y rubrica
    if request.method == 'POST':
        evaluadores = request.POST.getlist('evals')
        fecha_ini = request.POST.get('fecha_ini')
        fecha_fin = request.POST.get('fecha_fin')
        rub = request.POST.get('rubrica')
        nombre = request.POST.get('nombre')
        curso = Curso.objects.filter(nombre=request.POST.get('curso')).get()
        rubrica = Rubrica.objects.filter(nombre=rub).get()
        evaluacion = Evaluacion.objects.create(
            nombre=nombre,
            fecha_inicio=fecha_ini,
            fecha_fin=fecha_fin
        )
        evaluacion.curso=curso
        evaluacion.rubrica = rubrica
        evaluacion.save()
        for eva in evaluadores:
            evaluacion.evaluadores.add(Evaluador.objects.filter(email=eva).get())
    return redirect('/a/eval/')
