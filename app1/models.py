from pyexpat import model
from django.db import models

# Create your models here.
class Usuario(models.Model):
    id= models.AutoField(primary_key=True)
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    telefono= models.CharField(max_length=25)