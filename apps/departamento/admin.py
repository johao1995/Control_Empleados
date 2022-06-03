from django.contrib import admin
from .models import Departamento

class DepartamentoAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'departamento',
        'area',
        'fecha'
    )

admin.site.register(Departamento,DepartamentoAdmin)