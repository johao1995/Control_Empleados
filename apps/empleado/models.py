from django.db import models
from apps.departamento.models import Departamento
from .managers import EmpleadoManager

class Habilidad(models.Model):
    name=models.CharField(max_length=30,blank=False,verbose_name='Habilidad')

    class Meta:
        verbose_name_plural='Habilidad'
        db_table='habilidad'

    def __str__(self):
        return self.name

class Empleado(models.Model):
    first_name=models.CharField(max_length=30,blank=False,verbose_name='Nombre')
    last_name=models.CharField(max_length=30,blank=False,verbose_name='Apellidos')
    puesto=models.CharField(max_length=30,blank=False,verbose_name='Puesto')
    codigo_departamento=models.ForeignKey(Departamento,on_delete=models.CASCADE,verbose_name='Departamento')
    habilidad=models.ManyToManyField(Habilidad,verbose_name='Habilidad')
    image=models.ImageField(upload_to='empleado/img',verbose_name='Imagen')
    fecha=models.DateField(verbose_name='Fecha Registro')
    objects=EmpleadoManager()
    
    class Meta:
        verbose_name_plural='Empleado'
        db_table='empleado'
    
    def __str__(self):
        return self.first_name