from django.urls import path
from . import views
api_departamento=([
    path('lista-api_departamento/',views.ListaApiDepartamento.as_view(),name='lista-api_departamento'),
    path('detalle-api_departamento/<pk>',views.DetalleApiDepartamento.as_view(),name='detalle-api_departamento')
],'api_departamento')