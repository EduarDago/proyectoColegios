# -*- coding: utf-8 -*-
from django.db import models
from Apps.Grado.models import Grado


class Grupo(models.Model):
	idGrupo = models.CharField(primary_key=True, max_length=40)
	foraneaGrado = models.ForeignKey(Grado, null=True,blank=True, on_delete=models.CASCADE)
	
	def __str__(self):
		return '{}'.format(self.idGrupo)
	

