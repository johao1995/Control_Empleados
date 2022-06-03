from rest_framework import generics
from apps.departamento.models import Departamento
from .serializers import DepartamentoSerializer

class ListaApiDepartamento(generics.ListAPIView):
    serializer_class=DepartamentoSerializer

    def get_queryset(self):
        lista_departamento=Departamento.objects.all()
        return lista_departamento

class DetalleApiDepartamento(generics.RetrieveAPIView):
    serializer_class=DepartamentoSerializer
    queryset=Departamento.objects.all()
