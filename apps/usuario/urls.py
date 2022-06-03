from django.urls import path
from . import views

usuario_urlpatterns=([
    path('',views.HomePage.as_view(),name='home')
],'usuario')