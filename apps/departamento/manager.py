from django.db import models

class DepartamentoManager(models.Manager):
    def lista_departamentos(self):
        departamento=self.all()
        return departamento
