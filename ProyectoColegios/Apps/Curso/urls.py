__author__ = "Juan Pablo Aguirre Chica"
__copyright__ = "Copyright 2018, ISUC"

# -*- coding: utf-8 -*-


from django.conf.urls import url

from Apps.Curso.views import CrearCurso, ConsultarCurso, ActualizarCurso, EliminarCurso, mostrarContenidoCurso


urlpatterns = [
    url(r'^CrearCurso/', CrearCurso.as_view(), name='CrearCurso'),
    url(r'^ConsultarCurso/', ConsultarCurso.as_view(), name='ConsultarCurso'),
    url(r'^ActualizarCurso/(?P<pk>\d+)/$', ActualizarCurso.as_view(), name='ActualizarCurso'),
    url(r'^EliminarCurso/(?P<pk>\d+)/$', EliminarCurso.as_view(), name='EliminarCurso'),
    url(r'^GUIGestionContenidoCurso/(?P<idCurso>\d+)/$',mostrarContenidoCurso,name='GUIGestionContenidoCurso'), #Recuerden que se tiene que asociar a otro template
]
