from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import Group, User
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect


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
        user = User.objects.create_user(mail, mail, password)

        ev_group, _ = Group.objects.get_or_create(name='evaluadores')
        user.groups.add(ev_group)


        Evaluador.objects.create(
            user=user,
            nombre=name,
            apellido=lname,
            email=user.email
        )

    evaluadores = Evaluador.objects.all()

    return render(request, 'Admin_interface/Evaluadores_admin.html', context={'evaluadores': evaluadores})

def delete_evaluador(request):
    mail_to_delete = request.POST.get('evaluador')
    Evaluador.objects.filter(email = mail_to_delete).delete()
    return redirect('/a/ev/')

def modify_evaluador(request):
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


