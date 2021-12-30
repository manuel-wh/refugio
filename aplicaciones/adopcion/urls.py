from django.conf.urls import url
from aplicaciones.adopcion.views import index_adopcion, SolicitudList, SolicitudCreate, solicitud_listar, \
    solicitud_crear

urlpatterns = [
url(r'^solicitud/class/listar$', SolicitudList.as_view(), name='solicitud_listar'),
url(r'^solicitud/class/crear$', SolicitudCreate.as_view(), name='solicitud_crear'),
url(r'^solicitud/funcion/listar$', solicitud_listar, name='solicitud_listarFuncion'),
url(r'^solicitud/funcion/crear$', solicitud_crear, name='solicitud_crearFuncion'),

]