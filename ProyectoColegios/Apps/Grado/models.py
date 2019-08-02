# -*- coding: utf-8 -*-
from django.db import models


class Grado(models.Model):
	idGrado = models.CharField(primary_key=True, max_length=40)
	
	def __str__(self):
		return '{}'.format(self.nombre)
