from django.db import models

class Funcionario(models.Model):
    nombre = models.CharField(50)
    apellido = models.CharField(50)
    correo = models.CharField(100)
    telfono = models.CharField(50)
    perfil = models.CharField(50)


    def __str__(self) :
        return f'{self.nombre} {self.apellido}-{self.correo}-{self.telfono}-{self.perfil}'
    


