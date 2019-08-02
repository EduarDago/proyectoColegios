# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from Apps.Profesor.models import Profesor

__author__      = "Eduard"
__copyright__   = "Copyright 2018, ISUC"


class formProfesor(UserCreationForm):
	
	cedula = forms.CharField(max_length=14, required=True)
	profesion = forms.CharField(max_length=140, required=False, label='Profesión')
	telefono = forms.CharField(max_length=14, required=False)
	codigoprofesor = forms.CharField(max_length=14, required=False, label='Código del profesor')
	
	class Meta:
		model = User
		fields = [
			'username',
			'email',
			'first_name',
			'last_name',
			'password1',
			'password2',
		]
		
		labels = {
			'username' : 'Usuario',
			'email' : 'Email',
			'first_name' :'Nombre',
			'last_name' : 'Apellido',
			'password1' : 'Contaseña',
			'password2' : 'Contraseña (confirmación)',
		}
		
		help_texts = {
			'username': 'requerido. 150 caracteres o menos. letras, digitos y @',
		} 

		
		
		
		