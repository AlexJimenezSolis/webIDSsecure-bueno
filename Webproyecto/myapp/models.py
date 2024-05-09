from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class PreguntaNoRespondida(models.Model):
    correo = models.EmailField(max_length=255)
    pregunta = models.TextField(max_length=255)

    def __str__(self):
        return self.pregunta