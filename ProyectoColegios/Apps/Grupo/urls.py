__author__      = "Nodier Jose Pineda Villa"
__copyright__   = "Copyright 2018, INSUC"

# -*- coding: utf-8 -*-


from django.conf.urls import url

from Apps.Grado.views import CrearGrado,EliminarGrado,ConsultarGrado,ActualizarGrado

urlpatterns=[url(r'^CrearGrado',CrearGrado.as_view(),name='CrearGrado'),
             url(r'^EliminarGrado/(?P<pk>\d+)/$',EliminarGrado.as_view(),name='EliminarGrado'),
             url(r'^ConsultarGrado',ConsultarGrado.as_view(),name='ConsultarGrado'),
             url(r'^ActualizarGrado/(?P<pk>\d+)/$',ActualizarGrado.as_view(),name='ActualizarGrado'),]

