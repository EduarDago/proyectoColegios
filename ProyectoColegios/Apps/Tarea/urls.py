__author__      = "Luis David Montoya Diaz"
__copyright__   = "Copyright 2018, ISUC"

# -*- coding: utf-8 -*-


from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from Apps.Tarea.views import ConsultarTarea, CrearTarea, ConsultarTodasTareas, descargarArchivo

urlpatterns=[
		url(r'^CrearTarea/(?P<idCurso>\d+)/$',CrearTarea.as_view(),name='CrearTarea'),
		#url(r'^EliminarTarea/(?P<pk>\d+)/$',EliminarEstudiante.as_view(),name='EliminarTarea'),
		url(r'^ConsultarTarea/(?P<pk>\d+)',ConsultarTarea.as_view(),name='ConsultarTarea'),
		#url(r'^ConsultarTodasTareas',ConsultarTodasTareas.as_view(),name='ConsultarTodasTareas'),
		#url(r'^ActualizarTarea/(?P<pk>\d+)/$',ActualizarEstudiante.as_view(),name='ActualizarTarea'),
		url(r'^ConsultarTodasTareas/(?P<codigoEstudiante>\d+)/$',ConsultarTodasTareas,name='ConsultarTodasTareas'), #Recuerden que se tiene que asociar a otro template
		url(r'^DescargarArchivo/(?P<pk>\d+)/$', descargarArchivo ,name='DescargarArchivo'),
		

]

#if settings.DEBUG:
#	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
