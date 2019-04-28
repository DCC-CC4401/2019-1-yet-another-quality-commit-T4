from django.shortcuts import render

# Create your views here.
def evaluacion(request):
    return render(request, 'Eval_interface/evaluacion.html')

def evadmin(request):
    return render(request, 'Eval_interface/evaluacionadmin.html')

def evmobile(request):
    return render(request, 'Eval_interface/evaluacionMobile.html')

def postev(request):
    return render(request, 'Eval_interface/postevaluacion.html')

def postevadmin(request):
    return render(request, 'Eval_interface/postevaluacionadmin.html')

def evaluacionesadmin(request):
    return render(request, 'Admin_interface/Evaluaciones_admin.html')