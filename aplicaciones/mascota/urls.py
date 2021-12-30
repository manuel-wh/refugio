from django.conf.urls import url, include

from aplicaciones.mascota.views import index, mascota_create, mascota_list, mascota_edit, mascota_delete, \
    MascotaList, MascotaCreate, MascotaUpdate, MascotaDelete

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^funcion/nuevo$', mascota_create , name= 'mascota_crearFunction'),
    url(r'^funcion/listar$', mascota_list, name= 'mascota_listarFunction'),
    url(r'^funcion/editar/(?P<id_mascota>\d+)/$', mascota_edit, name= 'mascota_editarFunction'),
    url(r'^funcion/eliminar/(?P<id_mascota>\d+)/$', mascota_delete, name= 'mascota_eliminarFunction'),
    url(r'^clase/nuevo$', MascotaCreate.as_view() , name= 'mascota_crear'),
    url(r'^clase/listar$', MascotaList.as_view(), name= 'mascota_listar'),
    url(r'^clase/editar/(?P<pk>\d+)/$', MascotaUpdate.as_view(), name= 'mascota_editar'),
    url(r'^clase/eliminar/(?P<pk>\d+)/$', MascotaDelete.as_view(), name= 'mascota_eliminar'),

]
