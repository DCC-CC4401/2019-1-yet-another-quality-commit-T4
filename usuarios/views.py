from django.contrib.auth import authenticate, logout, login
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from django.urls import reverse


def login_view(request):
    return render(request, 'usuarios/login.html')


def process_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            # return HttpResponseRedirect('administrador:landing')
            return redirect('administrador:landing')
        else:
            return render(request, 'usuarios/login.html', {
            'error_message': "Quien eri vo xD",
        })

    logout(request)

    return HttpResponse('Hola que tal')
