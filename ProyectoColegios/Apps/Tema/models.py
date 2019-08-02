# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

from Apps.MateriaGrado.models import MateriaGrado


# 
class Tema(models.Model):
	idTema = models.CharField(primary_key=True, max_length=40)
	nombreTema = models.CharField(max_length=20)
	descripcionTema = models.TextField(max_length=200)
	foraneaMateriaGrado = models.ForeignKey(MateriaGrado, null=True, blank=True, on_delete=models.CASCADE)

	def __str__(self):
		return '{}'.format(self.nombreTema)