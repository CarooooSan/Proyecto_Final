from django.db import models

# Create your models here.

class Encuesta(models.Model):
    
    util_agenda= models.CharField(max_length=3)  # Sí/No
    rendimiento= models.CharField(max_length=3)  # Sí/No
    tono_bajo_alertas = models.CharField(max_length=3)  # Sí/No
    herramientas = models.CharField(max_length=100) 
    alcance = models.CharField(max_length=50)
    experiencia = models.CharField(max_length=3)  # Sí/No/Tal vez
    personal_interno_externo = models.CharField(max_length=100)
    autenticacion_dos_factores = models.CharField(max_length=100)  # Sí/No/Tal vez
    monitoreo_seguridad_constante = models.CharField(max_length=3)  # Sí/No/Tal vez

    def __str__(self):
        return self.aplicacion
