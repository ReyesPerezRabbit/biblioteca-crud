from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portafolio/images/')
