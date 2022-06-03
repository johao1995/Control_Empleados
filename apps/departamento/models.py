from django.db import models 
from .manager import DepartamentoManager

class Departamento(models.Model):
    area_choices=(
        ('A-DW','Desarrollo Web'),
        ('A-RC','Redes y Comunicacion'),
        ('A-AS','Analista Sistemas')
    )
    departamento=models.CharField(max_length=30,blank=False,verbose_name='Nombre')
    area=models.CharField(max_length=5,choices=area_choices,blank=False,verbose_name='Area')
    fecha=models.DateField(verbose_name='Fecha Creacion')
    objects=DepartamentoManager()
    
    class Meta:
        verbose_name_plural='departamento'
        db_table='departamento'

    def __str__(self):
        return self.departamento
