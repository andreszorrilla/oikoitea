"""oikoitea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.views import logout, login
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^logout/$', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    url(r'^accounts/login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),

    #url(r'^personas/', include('apps.personas.urls', namespace='personas')),
    url(r'^perfil/', include('apps.perfil.urls', namespace='perfil')),
    url(r'^pacientes/', include('apps.pacientes.urls', namespace='pacientes')),
    url(r'^actividades/', include('apps.actividades.urls', namespace='actividades')),
    url(r'^imagenes/', include('apps.fotos.urls', namespace='imagenes')),
    url(r'', include('apps.home.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



if settings.DEBUG:
    urlpatterns += static(
                        settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT
                    )