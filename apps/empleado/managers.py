from django.db import models

class EmpleadoManager(models.Manager):
    def lista_empleados(self):
        list_empleado=self.all()
        return list_empleado
    
    def busqueda_empleado(self,empleado):
        busqueda_emp=self.filter(first_name__contains=empleado)
        return busqueda_emp
    
    def detalle_empleado(self,pk):
        detall_emp=self.get(pk=pk)
        return detall_emp