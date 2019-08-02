# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Materia(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    nombre = models.CharField(max_length=50)
    intensidad = models.PositiveIntegerField()
#returna el nombre de la materia en campos de seleccion
    def __str__(self):
        return '{}'.format(self.nombre)
