from django.urls import path
from . import views
departamento_urlpatterns=([
    path('lista-departamento/',views.ListDepartamento.as_view(),name='lista-departamento'),
    path('departamento-empleado/<pk>',views.DetalleDepartamento.as_view(),name='departamento-empleado')
],'departamento')