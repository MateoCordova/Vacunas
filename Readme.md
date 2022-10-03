# Aplicación de vacunas
Esta aplicación en Django permite a un administrador crear empleados. Estos empleados pueden ingresar al portal para registrar su información de vacunación.
Los administradores pueden filtrar esta información

## Instalación
```
#opcional
py -m venv .venv
$ .venv/Scripts/Activate.ps1
#obligario
pip install requirements.txt
cd mysite
py .\manage.py runserver
```

## Administrador
El user demo ingresa a http://127.0.0.1:8000/admin/login/. Usar las credenciales del archivo usersEjemplo.txt
Cuando se crea un usuario, su usuario y su contraseña se imprime en consola. (En un ambiente productivo, se enviaría por correo.)

## Empleado
El user ingresa a http://127.0.0.1:8000. El user solo puede ver su información.