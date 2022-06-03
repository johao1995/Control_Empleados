from django.urls import path
from . import views

api_empleado=([
    path('lista-api_empleado/',views.ListaApiEmpleado.as_view(),name='lista-api_empleado'),
    path('detalle-api_empleado/<pk>',views.DetalleApiEmpleado.as_view(),name='detalle-api_empleado'),
    path('detalle-api_empleado-habilidad/<pk>',views.DetalleApiHabilidad.as_view(),name='detalle-api_empleado-habilidad')
],'api_empleado')