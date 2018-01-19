# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


from .models import Foto, DescripcionFoto
from django.views.generic import ListView



from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView, CreateView , UpdateView, DeleteView #, TemplateView, View
from django.views.generic.detail import SingleObjectMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.urls import reverse_lazy
from django.db import transaction
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.db.models import Q, Sum, F


class FotoListView(ListView):
    model = Foto
    # template_name = 'fotos/paciente_index.html' #default paciente list

    def get_context_data(self, **kwargs):
        context = super(FotoListView, self).get_context_data(**kwargs)
        filtro = self.request.GET['filtro'] if 'filtro' in self.request.GET else ''

        if filtro == '':
            fotos = Foto.objects.all()[:500][::-1] 
        else:
            params = Q(nombre_archivo__contains=filtro)
            fotos = Foto.objects.filter( params )[:500][::-1] 
        context['fotos'] = fotos
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FotoListView, self).dispatch(*args, **kwargs)
