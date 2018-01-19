# -*- encoding: utf-8 -*-

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

from .forms import PacienteForm
from .models import *



#nro de elementos para paginar
paginate = 10


class PacienteMixin(object):
    model = Paciente


class PacienteListView(ListView):
    model = Paciente
    # template_name = 'pacientes/paciente_index.html' #default paciente list

    def get_context_data(self, **kwargs):
        context = super(PacienteListView, self).get_context_data(**kwargs)
        filtro = self.request.GET['filtro'] if 'filtro' in self.request.GET else ''

        if filtro == '':
            pacientes = Paciente.objects.all()
        else:
            params = Q(nombres__contains=filtro) | Q(apellidos__icontains=filtro)
            pacientes = Paciente.objects.filter( params )
        context['pacientes'] = pacientes
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PacienteListView, self).dispatch(*args, **kwargs)



class PacienteCreate(PacienteMixin, CreateView):
    form_class = PacienteForm


class PacienteUpdate(PacienteMixin, UpdateView):
    form_class = PacienteForm


class PacienteDetail(PacienteMixin, DetailView):
    pass


class PacienteDelete(PacienteMixin, DeleteView):
    pass