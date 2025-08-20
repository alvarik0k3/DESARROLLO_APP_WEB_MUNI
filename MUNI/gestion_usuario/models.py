from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.CharField(max_length=100)
    telfono = models.CharField(max_length=50)
    perfil = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=100)


    def __str__(self) :
        return f'{self.nombre} {self.apellido}-{self.correo}-{self.telfono}-{self.perfil}'
    


