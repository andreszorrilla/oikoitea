# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView, CreateView , UpdateView, DeleteView #, TemplateView, View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.forms import modelformset_factory
from django.http import HttpResponseRedirect, JsonResponse

from .models import Actividad, ActividadDetalle
from .forms import ActividadForm, ActividadDetalleForm
from django.template import RequestContext
from django.conf import settings
import random

from el_pagination.views import AjaxListView

		
class ActividadListView(AjaxListView):
    page_template='actividades/actividad_list_page.html'
    model = Actividad
    # template_name = 'actividades/paciente_index.html' #default paciente list

    def get_context_data(self, **kwargs):
        context = super(ActividadListView, self).get_context_data(**kwargs)
        actividades = Actividad.objects.all()
        context['actividades'] = actividades
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ActividadListView, self).dispatch(*args, **kwargs)



class ActividadMixin(object):
    model = Actividad

class ActividadCreate(ActividadMixin, CreateView):
    form_class = ActividadForm


class ActividadUpdate(ActividadMixin, UpdateView):
    form_class = ActividadForm

class ActividadDetail(ActividadMixin, DetailView):
    pass

class ActividadDelete(ActividadMixin, DeleteView):
    pass


#@login_required
def actividad_create(request):
    ActividadDetalleFormSet = modelformset_factory(ActividadDetalle, form=ActividadDetalleForm, extra=1, can_delete=True, can_order=True)
    if request.method == 'POST':
        actividadForm = ActividadForm(request.POST)
        formset = ActividadDetalleFormSet(request.POST, request.FILES,
                                        queryset=ActividadDetalle.objects.none())
        if actividadForm.is_valid() and formset.is_valid():
            actividad_form = actividadForm.save(commit=False)
            actividad_form.user = request.user
            actividad_form.save()

            for form in formset.cleaned_data:
                imagen      = form['imagen']
                descripcion = form['descripcion']
                detalle = ActividadDetalle(actividad=actividad_form, imagen=imagen, descripcion=descripcion)
                detalle.save()
            #messages.success(request,"Yeeew,check it out on the home page!")
            return HttpResponseRedirect(reverse("actividad:actividades_index"))
        else:
            print actividadForm.errors, formset.errors
    else:
        actividadForm = ActividadForm()
        formset = ActividadDetalleFormSet(queryset=ActividadDetalle.objects.none())
    return render(request, 'actividades/actividad_form.html',
                  {'actividadForm': actividadForm, 'formset': formset},
                  RequestContext(request))

#@login_required
def actividad_load_photo(request):
    num = str(random.randint(1, 6))
    url = settings.MEDIA_URL + "ejemplos/" + str(num) + ".jpg"
    return JsonResponse({'url':url})


def actividad_change_estado(request):
    id = request.GET['id']
    actividad_detalle = ActividadDetalle.objects.get(pk=id)
    estados = ['SE', 'AC', 'LO', 'NL', 'IN']
    estado_idx = (estados.index(actividad_detalle.estado) + 1) % len(estados)
    actividad_detalle.estado = estados[estado_idx]
    actividad_detalle.save()
    return JsonResponse({"estado": estados[estado_idx]})



def actividad_fotos(request):
    if request.method == 'POST':
        actividadDetalleForm = ActividadDetalleForm(request.POST)
        if actividadDetalleForm.is_valid():
            actividad_form = actividadDetalleForm.save(commit=False)
            imagen      = actividad_form['imagen']
            descripcion = actividad_form['descripcion']
            detalle = ActividadDetalle(actividad=actividad_form, imagen=imagen, descripcion=descripcion)
            detalle.save()
            actividad_form.save()
            return HttpResponseRedirect(reverse("actividad:actividades_index"))
        else:
            print actividadDetalleForm.errors, formset.errors
    else:
        actividadDetalleForm = ActividadDetalleForm()
    return render(request, 'actividades/actividad_foto.html',
                  {'actividadDetalleForm': actividadDetalleForm},
                  RequestContext(request))

