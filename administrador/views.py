from django.shortcuts import render, redirect
from evaluaciones.models import Evaluador
from django.utils.crypto import get_random_string

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
    return render(request, 'Admin_interface/Evaluaciones_admin.html')