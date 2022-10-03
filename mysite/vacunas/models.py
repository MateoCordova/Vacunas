from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

import re

def verificar(nro):
    l = len(nro)
    if l == 10 or l == 13: # verificar la longitud correcta
        cp = int(nro[0:2])
        if cp >= 1 and cp <= 22: # verificar codigo de provincia
            tercer_dig = int(nro[2])
            if tercer_dig >= 0 and tercer_dig < 6 : # numeros enter 0 y 6
                if l == 10:
                    return __validar_ced_ruc(nro,0)                       
                elif l == 13:
                    return __validar_ced_ruc(nro,0) and nro[10:13] != '000' # se verifica q los ultimos numeros no sean 000
            elif tercer_dig == 6:
                return __validar_ced_ruc(nro,1) # sociedades publicas
            elif tercer_dig == 9: # si es ruc
                return __validar_ced_ruc(nro,2) # sociedades privadas
            else:
                raise ValidationError(_('Tercer dígito incorrecto')) 
        else:
            raise ValidationError(_('Codigo de provincia incorrecto'))  
    else:
        raise ValidationError(_('Longitud incorrecta del numero ingresado'))

def __validar_ced_ruc(nro,tipo):
    total = 0
    if tipo == 0: # cedula y r.u.c persona natural
        base = 10
        d_ver = int(nro[9])# digito verificador
        multip = (2, 1, 2, 1, 2, 1, 2, 1, 2)
    elif tipo == 1: # r.u.c. publicos
        base = 11
        d_ver = int(nro[8])
        multip = (3, 2, 7, 6, 5, 4, 3, 2 )
    elif tipo == 2: # r.u.c. juridicos y extranjeros sin cedula
        base = 11
        d_ver = int(nro[9])
        multip = (4, 3, 2, 7, 6, 5, 4, 3, 2)
    for i in range(0,len(multip)):
        p = int(nro[i]) * multip[i]
        if tipo == 0:
            total+=p if p < 10 else int(str(p)[0])+int(str(p)[1])
        else:
            total+=p
    mod = total % base
    val = base - mod if mod != 0 else 0
    if val != d_ver:
        raise ValidationError(_('Cedula no válida'))
    return

def soloLetras(val):
    patron = re.compile("^[a-zA-Z\sáéíóúÁÉÍÓÚ]*$")
    if patron.match(val):
        return
    raise ValidationError(_('No puede incluir números ni caracteres especiales'))

class TipoVacuna(models.Model):
    marca = models.CharField(max_length=20)
    def __str__(self):
        return self.marca

class Empleado(models.Model):
    cedula = models.CharField(max_length=10,validators=[verificar])
    nombres = models.CharField(max_length=60,validators=[soloLetras])
    apellidos = models.CharField(max_length=60,validators=[soloLetras])
    correo_electronico = models.EmailField()
    vacunado = models.BooleanField(default=False)
    fecha_nacimiento = models.DateField('Fecha de nacimiento', null=True)
    direccion =  models.CharField(max_length=100, null=True)
    telefono = models.TextField(max_length=10,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    #account = models.ForeignKey(Users)
    def __str__(self):
        return '{0} {1}'.format(self.nombres,self.apellidos)
    def fecha_nacimiento_formato(self):
        return '{0}-{1:02d}-{2:02d}'.format(self.fecha_nacimiento.year,self.fecha_nacimiento.month,self.fecha_nacimiento.day)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['cedula'], name='unique cedula')
        ]
    
class VacunaEmpleado(models.Model):
    fecha = models.DateField()
    dosis_N = models.IntegerField()
    tipo_vacuna = models.ForeignKey(TipoVacuna, on_delete=models.CASCADE)
    empleado = models.OneToOneField(
        Empleado,
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return "\n{0}.- {1} el {2}".format(self.dosis_N,self.tipo_vacuna.marca,self.fecha) 
    def fecha_formato(self):
        return '{0}-{1:02d}-{2:02d}'.format(self.fecha.year,self.fecha.month,self.fecha.day)
    