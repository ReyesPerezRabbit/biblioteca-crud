from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tasks(models.Model):
    title = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    creacion = models.DateTimeField(auto_now_add=True)
    completado = models.DateTimeField(null = True, blank=True)
    importante = models.BooleanField(default=False)
    user = models.ForeignKey(User , on_delete=models.CASCADE)

    def __str__(self) :
        return self.title + ' - by ' + self.user.username