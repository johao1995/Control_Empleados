from django.db import models

class EmpleadoApiManager(models.Manager):
    def lista_apiempleado(self):
        lista_apiemp=self.all()
        return lista_apiemp