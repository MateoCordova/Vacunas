from django.contrib import admin
from .models import Empleado,TipoVacuna
from django.contrib.auth.models import User, Group
from rangefilter.filters import DateRangeFilter
import random
import string

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    exclude = ('vacunas',
    'vacunado',
    'fecha_nacimiento',
    'direccion',
    'telefono',
    'user')
    def save_model(self, request, obj, form, change):
        print(change)
        usuario = obj.nombres[0:2] + obj.apellidos.split()[0]
        contraseña = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 5))
        user = User.objects.create_user(usuario, obj.correo_electronico, contraseña)
        print(user)
        print(contraseña)
        user.groups.add(1)
        user.save()
        obj.user = user
        super().save_model(request, obj, form, change)
    list_filter = ['vacunado', 'vacunaempleado__tipo_vacuna__marca',
    ('vacunaempleado__fecha',DateRangeFilter)]
admin.site.register(TipoVacuna)
admin.site.unregister(User)
admin.site.unregister(Group)

