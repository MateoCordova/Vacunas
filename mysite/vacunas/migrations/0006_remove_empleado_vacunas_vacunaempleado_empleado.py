# Generated by Django 4.1.1 on 2022-10-02 01:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vacunas', '0005_remove_empleado_contraseña_remove_empleado_usuario_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empleado',
            name='vacunas',
        ),
        migrations.AddField(
            model_name='vacunaempleado',
            name='empleado',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='vacunas.empleado'),
            preserve_default=False,
        ),
    ]
