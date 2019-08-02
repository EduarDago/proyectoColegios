__author__      = "Luis David Montoya Diaz"
__copyright__   = "Copyright 2018, ISUC"

# -*- coding: utf-8 -*-


from django.conf.urls import url

from Apps.Estudiante.views import CrearEstudiante,EliminarEstudiante,ConsultarEstudiante,ActualizarEstudiante

urlpatterns=[url(r'^CrearEstudiante',CrearEstudiante.as_view(),name='CrearEstudiante'),
             url(r'^EliminarEstudiante/(?P<pk>\d+)/$',EliminarEstudiante.as_view(),name='EliminarEstudiante'),
             url(r'^ConsultarEstudiante',ConsultarEstudiante.as_view(),name='ConsultarEstudiante'),
             url(r'^ActualizarEstudiante/(?P<pk>\d+)/$',ActualizarEstudiante.as_view(),name='ActualizarEstudiante'),]

