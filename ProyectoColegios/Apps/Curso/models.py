__author__      = "Juan Pablo Aguirre Chica"
__copyright__   = "Copyright 2018, ISUC"

from django.db import models
from Apps.Profesor.models import Profesor 
from Apps.MateriaGrado.models import MateriaGrado
from Apps.Grupo.models import Grupo


# Create your models here.
"""
	Clase que define el modelo Curso
	
	Parámetros:

    idCurso -- identificador unico del curso
    foraneaProfesor -- identificador del modelo Profesor asociado al curso
    foraneaMateriaGrado -- identificador del modelo MateriaGrado asociado al curso
	foraneaGrupo -- identificador del modelo Curso asociado al curso

"""
class Curso(models.Model):
	idCurso = models.CharField(primary_key=True, max_length=40)
	foraneaProfesor = models.ForeignKey(Profesor,null=True,blank=True, on_delete=models.CASCADE)
	foraneaMateriaGrado = models.ForeignKey(MateriaGrado,null=True,blank=True, on_delete=models.CASCADE)
	foraneaGrupo = models.ForeignKey(Grupo,null=True,blank=True, on_delete=models.CASCADE)
 	
	""" 
		Función que permite retornar al modelo o vista asociada a un Curso, 
		el identificador respectivo de este modelo.
	
	"""
	def __str__(self):
		return '{}'.format(self.idCurso)


