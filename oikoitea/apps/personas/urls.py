from django.conf.urls import url

from . import views

app_name = 'personas'
urlpatterns = [
    url(r'^$', views.profesionales_index, name='profesionales_index'),
]
