from django.conf.urls import url
from .views import PacienteListView, PacienteDetail, PacienteCreate, PacienteUpdate, PacienteDelete

app_name = 'paciente'

urlpatterns = [
    url(r'^$', 
    	PacienteListView.as_view(), 
    	name='paciente_index'
    ),
    url(
        regex=r'^(?P<pk>\d+)$',
        view=PacienteDetail.as_view(),
        name="paciente_detail"
    ),
    url(
        r'new/$', 
        PacienteCreate.as_view(),
        name='paciente_new'
    ),
    url(
        r'(?P<pk>[0-9]+)/edit/$', 
        PacienteUpdate.as_view(),
        name='paciente_edit'
    ),
    url(
        r'(?P<pk>[0-9]+)/delete/$', 
        PacienteDelete.as_view(),
        name='paciente_delete'
    ),

]
