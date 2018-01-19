from django.conf.urls import url

from . import views

app_name = 'perfil'

urlpatterns = [
    url(r'^u/(?P<username>[a-zA-Z0-9]+)$', views.get_user_profile, name="perfil_username"),
    url(r'update/$', views.update_profile, name='update_user'),

]