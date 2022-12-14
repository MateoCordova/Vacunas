# Generated by Django 4.1.1 on 2022-10-03 17:41

from django.db import migrations, models
import vacunas.models


class Migration(migrations.Migration):

    dependencies = [
        ('vacunas', '0009_alter_empleado_cedula'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='apellidos',
            field=models.CharField(max_length=60, validators=[vacunas.models.soloLetras]),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='nombres',
            field=models.CharField(max_length=60, validators=[vacunas.models.soloLetras]),
        ),
    ]
