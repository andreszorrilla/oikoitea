from django.conf.urls import url
from .views import ActividadListView, ActividadCreate, ActividadUpdate, ActividadDetail, ActividadDelete
from . import views

app_name = 'actividad'

urlpatterns = [

    url(r'^$', 
    	ActividadListView.as_view(),
    	name='actividades_index'
    ),
    url(
        regex=r'^(?P<pk>\d+)$',
        view=ActividadDetail.as_view(),
        name="actividad_detail"
    ),
    url(
        r'new/$', 
        views.actividad_create,
        name='actividad_new'
    ),
    url(
        r'(?P<pk>[0-9]+)/edit/$', 
        ActividadUpdate.as_view(),
        name='actividad_edit'
    ),
    url(
        r'(?P<pk>[0-9]+)/delete/$', 
        ActividadDelete.as_view(),
        name='actividad_delete'
    ),
    url(
        r'actividad_load_photo/$', 
        views.actividad_load_photo,
        name='actividad_load_photo'
    ),
    url(
        r'^actividad_change_estado/$', 
        views.actividad_change_estado,
        name='actividad_change_estado'
    ),
    url(
        r'^fotos/$', 
        views.actividad_fotos,
        name='actividad_fotos'
    ),

]
