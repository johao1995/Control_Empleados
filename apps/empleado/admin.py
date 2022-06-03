from django.contrib import admin
from .models import Empleado,Habilidad

class EmpleadoAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'first_name',
        'last_name',
        'puesto',
        'codigo_departamento',
        'image',
        'fecha'
    )

admin.site.register(Empleado,EmpleadoAdmin)

class HabilidadAdmin(admin.ModelAdmin):
    list_display=(
        'name',
    )

admin.site.register(Habilidad,HabilidadAdmin)