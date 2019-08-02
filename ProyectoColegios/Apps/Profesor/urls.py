# -*- coding: utf-8 -*-

from django.conf.urls import url
from Apps.Profesor.views import CrearProfesor,cargarCursosProfesor


__author__      = "Eduard"
__copyright__   = "Copyright 2018, ISUC"

urlpatterns=[
	url(r'^CrearProfesor',CrearProfesor.as_view(),name='CrearProfesor'),
	#url(r'^EliminarProfesor/(?P<pk>\d+)/$',EliminarEstudiante.as_view(),name='EliminarProfesor'),
	#url(r'^ConsultarProfesor',ConsultarEstudiante.as_view(),name='ConsultarProfesor'),
	url(r'^ActualizarProfesor/(?P<codigoProfesor>\d+)/$',cargarCursosProfesor,name='ActualizarProfesor'), #Recuerden que se tiene que asociar a otro template

]