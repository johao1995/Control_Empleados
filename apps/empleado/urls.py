from django.urls import path
from . import views

empleado_urlpatterns=([
    path('register-empleado/',views.EmpleadoRegister.as_view(),name='register-empleado'),
    path('lista-empleado/',views.EmpleadoList.as_view(),name='lista-empleado'),
    path('admin-empleado/',views.EmpleadoAdmin.as_view(),name='admin-empleado'),
    path('update-empleado/<pk>',views.EmpleadoUpdate.as_view(),name='update-empleado'),
    path('delete-empleado/<pk>',views.EmpleadoDelete.as_view(),name='delete-empleado'),
    path('detalle-empleado/<pk>',views.detalle_empleado,name='detalle-empleado')
],'empleado')