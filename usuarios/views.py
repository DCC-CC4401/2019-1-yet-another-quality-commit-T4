from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import Group, User
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from evaluaciones.models import Evaluacion
from usuarios.models import Evaluador
from cursos.models import Curso
from rubricas.models import Rubrica

from usuarios.models import Evaluador
from django.utils.crypto import get_random_string


def login_view(request):
    return render(request, 'usuarios/login.html')


def process_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            # return HttpResponseRedirect(reverse('administrador:landing'))
            if Group.objects.get(name='administradores') in user.groups.all():

                return redirect('administrador:landing')
            # aca deberian ir mas ifs para los evaluadores
            elif Group.objects.get(name='evaluadores') in user.groups.all():
                return redirect('../e/lp/')
            else:
                return render(request, 'usuarios/login.html', {
                    'error_message': "Por ahora solo soporto admins",
                })
        else:
            return render(request, 'usuarios/login.html', {
            'error_message': "Quien eri vo xD",
            })

    logout(request)

    return HttpResponse('Hola que tal')


def evaluadores(request):
    if(request.method == 'POST'):
        name = request.POST.get('name')
        lname = request.POST.get('lname')
        mail = request.POST.get('mail')
        password = get_random_string(8)

        print(f'Se viene la contraseña de {name}: ', password)
        # el nombre de usuario de django sera el mail de nuestros usuarios para poder autenticar
        user = User.objects.create_user(username=mail, password=password)

        ev_group, _ = Group.objects.get_or_create(name='evaluadores')
        user.groups.add(ev_group)


        Evaluador.objects.create(
            user=user,
            nombre=name,
            apellido=lname,
        )

    evaluadores = Evaluador.objects.order_by('-id').all()

    return render(request, 'Admin_interface/Evaluadores_admin.html', context={'evaluadores': evaluadores})

def delete_evaluador(request):
    mail = request.POST.get('evaluador')
    User.objects.get(username = mail).delete()
    return redirect('/a/ev/')

def modify_evaluador(request):

    print('hooooooooooooooooooooolaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    new_name = request.POST.get('new_name')
    new_lname = request.POST.get('new_lname')
    new_mail = request.POST.get('new_mail')
    previous_mail = request.POST.get('evaluador')



    user = User.objects.get(username = previous_mail)
    evaluador = Evaluador.objects.get(user = user)

    if(new_name != ''):
        evaluador.nombre = new_name

    if(new_lname != ''):
        evaluador.apellido = new_lname

    if(new_mail != ''):
        evaluador.email = new_mail
        evaluador.user.username = new_mail

    evaluador.save()
    return redirect('/a/ev/')


def eval_loged(request):
    mail = request.user.get_username()
    d_user = User.objects.get(username=mail)
    evaluador = Evaluador.objects.get(user=d_user)
    print(evaluador.email)
    evaluaciones_ = Evaluacion.objects.filter(evaluadores=evaluador).order_by('-id')[:10]
    evaluadores_ = Evaluador.objects.all()
    cursos = Curso.objects.order_by('-id').all()
    rubricas = Rubrica.objects.order_by('-id').all()
    return render(request, 'Evaluador_interface/Landing_page_evaluador.html',
                  context={'evaluaciones': evaluaciones_, 'evaluadores': evaluadores_, 'cursos': cursos,
                           'rubricas': rubricas})



def evaluaciones_evaluador(request):
    mail = request.user.get_username()
    d_user = User.objects.get(username=mail)
    evaluador = Evaluador.objects.get(user=d_user)
    print(evaluador.email)
    evaluaciones_ = Evaluacion.objects.filter(evaluadores=evaluador).order_by('-id')
    evaluadores_ = Evaluador.objects.all()
    cursos = Curso.objects.order_by('-id').all()
    rubricas = Rubrica.objects.order_by('-id').all()
    return render(request, 'Evaluador_interface/evaluacion_evaluador.html',
                  context={'evaluaciones': evaluaciones_, 'evaluadores': evaluadores_, 'cursos': cursos,
                           'rubricas': rubricas})
