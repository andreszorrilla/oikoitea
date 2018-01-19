from django.conf.urls import url
from .views import *

app_name = 'imagen'


from django.conf.urls import url
from .views import *
from . import views

urlpatterns = [

    url(r'^$', 
        FotoListView.as_view(), 
        name='imagenes_index'
    ),
]
