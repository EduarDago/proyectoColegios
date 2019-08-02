# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from Apps.Grado.models import Grado

# Create your models here.


class MateriaGrado(models.Model):
    idMateriaGrado = models.CharField(max_length=50, primary_key=True)
    nombreMateria = models.CharField(max_length=50)
    foraneaGrado = models.ForeignKey(Grado, null=True,blank=True, on_delete=models.CASCADE)
	
#returna el nombre de la materia en campos de seleccion
    def __str__(self):
        return '{}'.format(self.nombreMateria)
