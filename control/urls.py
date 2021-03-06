"""control URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .settings import local
from apps.usuario.urls import usuario_urlpatterns
from apps.empleado.urls import empleado_urlpatterns
from apps.departamento.urls import departamento_urlpatterns
#apis
from apis.api_empleado.urls import api_empleado
from apis.api_departamento.urls import api_departamento

urlpatterns = [
    path('db-admin/', admin.site.urls),
    path('',include(usuario_urlpatterns)),
    path('empleado/',include(empleado_urlpatterns)),
    path('departamento/',include(departamento_urlpatterns)),
    #apis
    path('api_empleado/',include(api_empleado)),
    path('api_departamento/',include(api_departamento))
    
]

if local.DEBUG==True:
    from django.conf.urls.static import static
    urlpatterns+=static(local.MEDIA_URL,document_root=local.MEDIA_ROOT)