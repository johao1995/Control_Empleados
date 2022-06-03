from .serializers import EmpleadoSerializer,HabilidadSerializer
from rest_framework import generics
from apps.empleado.models import Empleado,Habilidad

class ListaApiEmpleado(generics.ListAPIView):
    serializer_class=EmpleadoSerializer
    
    def get_queryset(self):
        lista_emp=Empleado.objects.all()
        return lista_emp
    
class DetalleApiEmpleado(generics.RetrieveAPIView):
    serializer_class=EmpleadoSerializer
    queryset=Empleado.objects.all()

class DetalleApiHabilidad(generics.RetrieveAPIView):
    serializer_class=HabilidadSerializer
    queryset=Habilidad.objects.all()
    
