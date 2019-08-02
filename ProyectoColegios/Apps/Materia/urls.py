from django.conf.urls import url
from Apps.Materia.views import CrearMateria, ActualizarMateria, ListarMaterias, EliminarMateria


urlpatterns = [
    	url(r'^CrearMateria/', CrearMateria.as_view(), name='CrearMateria'),
    	url(r'^ActualizarMateria/(?P<pk>\d+)/$', ActualizarMateria.as_view(), name='ActualizarMateria'),
    	url(r'^ConsultarMateria/', ListarMaterias.as_view(), name='ConsultarMateria'),
    	url(r'^EliminarMateria/(?P<pk>\d+)/$', EliminarMateria.as_view(), name='EliminarMateria'),
    	]