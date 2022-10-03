
import re
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.template import loader
from .models import Empleado, TipoVacuna, VacunaEmpleado

from django.http import HttpResponse

def detail(request):
    if request.user.is_authenticated:
        logged = Empleado.objects.filter(user=request.user)[0]
        context = {
            'empleado': logged,
        }
        print(logged)
        return render(request, 'vacunas/detail.html', context)
    else:
        return redirect('accounts/login')
def edit(request):
    if request.user.is_authenticated:
        logged = Empleado.objects.filter(user=request.user)[0]
        tipo_vacunas = TipoVacuna.objects.all()
        print(tipo_vacunas)
        context = {
            'empleado' : logged,
            'tipo_vacunas' : tipo_vacunas
        }
        print(logged)
        return render(request, 'vacunas/edit.html', context)
    else:
        return redirect('/accounts/login')

def save(request):
    if request.user.is_authenticated:
        logged = Empleado.objects.filter(user=request.user)[0]
        print(request.POST)
        logged.fecha_nacimiento = request.POST['fecha_nacimiento']
        logged.direccion = request.POST['direccion']
        logged.telefono = request.POST['telefono']
        if(request.POST['tipo_vacuna'] != '' and request.POST['tipo_vacuna'] !='-1'):
            if(VacunaEmpleado.objects.filter(empleado = logged)):
                logged.vacunaempleado.tipo_vacuna = TipoVacuna.objects.get(id=request.POST['tipo_vacuna'])
                logged.vacunaempleado.fecha = request.POST['fechaVacuna']
                logged.vacunaempleado.dosis_N = request.POST['dosis_N']
                logged.vacunado = True
                logged.vacunaempleado.save()
            else:
                marca_selected = TipoVacuna.objects.get(id=request.POST['tipo_vacuna'])
                vacuna = VacunaEmpleado(empleado = logged,
                 tipo_vacuna=marca_selected,
                 fecha =  request.POST['fechaVacuna'],
                 dosis_N = request.POST['dosis_N']
                 )
                vacuna.save()
                logged.vacunado = True 
        else:
            try:
                logged.vacunaempleado.delete()
            finally:
                logged.vacunado = False
        logged.save()
        return redirect('/vacunas/')
    else:
        return redirect('/accounts/login')

