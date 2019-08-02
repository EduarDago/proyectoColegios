from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Profesor(models.Model):
	
	usuario = models.OneToOneField(User, on_delete=models.CASCADE)
	cedula = models.IntegerField()
	profesion = models.CharField(max_length=100)
	telefono = models.IntegerField()
	codigoprofesor = models.IntegerField(primary_key=True)
	

	def __str__(self):
		return '{} {}'.format(self.cedula,self.profesion)
	
'''@receiver(post_save, sender=User)
	def crearProfesorPerfil(sender, instance, created, **kwargs):
		if created:
			Profesor.objects.create(usuario=instance)
		instance.profile.save()'''
	
