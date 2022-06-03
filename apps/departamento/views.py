from django.shortcuts import render
from .models import Departamento
from apps.empleado.models import Empleado
from django.views import generic

class ListDepartamento(generic.ListView):
    template_name='departamento/lista_departamento.html'
    context_object_name='departamentos'

    def get_queryset(self):
        lista_departamento=Departamento.objects.lista_departamentos()
        print(lista_departamento)
        return lista_departamento

class DetalleDepartamento(generic.View):
    template_name='departamento/departamento_empleado.html'
    context_object_name='departamento_empleado'

    def get(self,request,pk):
        departamento_emplado=Empleado.objects.filter(codigo_departamento=pk)
        context={
            'dept_emp':departamento_emplado,
            'title':'Lista de Empleados'
        }
        return render(request,self.template_name,context)




