from rest_framework import serializers
from apps.empleado.models import Empleado, Habilidad
from apis.api_departamento.serializers import DepartamentoSerializer

class EmpleadoSerializer(serializers.HyperlinkedModelSerializer):
    #codigo_departamento=DepartamentoSerializer()

    class Meta:
        model=Empleado
        fields=(
            'id',
            'first_name',
            'last_name',
            'puesto',
            'codigo_departamento',
            'habilidad',
            'image',    
            'fecha'
        )
        extra_kwargs={
            'codigo_departamento':{'view_name':'api_departamento:detalle-api_departamento','lookup_field':'pk'},
            'habilidad':{'view_name':'api_empleado:detalle-api_empleado-habilidad','lookup_field':'pk'}
        }

class HabilidadSerializer(serializers.ModelSerializer):
    class Meta:
        model=Habilidad
        fields=(
            'id',
            'name'
        )

    
