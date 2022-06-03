from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .forms import EmpleadoForm
from .models import Empleado

class EmpleadoList(generic.ListView):
    template_name='empleado/lista_empleado.html'
    context_object_name='empleados'
    
    def get_queryset(self):
        empleado=self.request.GET.get('txt_name','')
        lista_empleado=Empleado.objects.busqueda_empleado(empleado)
        return lista_empleado

class EmpleadoRegister(generic.CreateView):
    template_name='empleado/register_empleado.html'
    form_class=EmpleadoForm
    model=Empleado
    success_url=reverse_lazy('empleado:lista-empleado')

class EmpleadoUpdate(generic.UpdateView):
    template_name='empleado/update_empleado.html'
    form_class=EmpleadoForm
    model=Empleado
    success_url=reverse_lazy('empleado:lista-empleado')

class EmpleadoDelete(generic.DeleteView):
    template_name='empleado/delete_empleado.html'
    model=Empleado
    context_object_name='empleado'
    success_url=reverse_lazy('empleado:lista-empleado')

class EmpleadoAdmin(generic.ListView):
    template_name='empleado/administrar_empleado.html'
    context_object_name='admiempleado'

    def get_queryset(self):
        admin_empleado=Empleado.objects.lista_empleados()
        return admin_empleado


def detalle_empleado(request,pk):
    template_name='empleado/detalle_empleado.html'
    context={
        'detalle_emp':Empleado.objects.detalle_empleado(pk)
    }
    return render(request,template_name,context)

