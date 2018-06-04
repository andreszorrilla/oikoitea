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


from django.conf import settings


import numpy as np
from scipy import spatial
from heapq import heappush, heappop, heapify


class FotoListView(ListView):
    model = Foto
    def get_context_data(self, **kwargs):
        
        #buscar()

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







def buscar():

    heap = []


    text = "perro"
    if text == "q!":
        sys.exit(0)
    input_average = avg_feature_vector(text, model=settings.W2V_MODEL, num_features=300, index2word_set=settings.INDEX2WORD_SET)
    sim = 1 - spatial.distance.cosine(s1_afv, s2_afv)
    #similarities = list(map(lambda p: p[:2] + (1 - spatial.distance.cosine(input_average, p[2]) ,), averages))
    #most_similar_meme = sorted(similarities, key=lambda p: p[2], reverse=True)
    for av in averages:
        similarity = spatial.distance.cosine(input_average, av[2])
        heap.append((similarity, av[:2]))
    heapify(heap)
    count = 50
    for item in heap:
        #item                   = heappop(heap)
        cosine_sim              = item[0]
        dir_imagen, descripcion = item[1]
        print "{0}\t{1}\t{2}".format(cosine_sim, dir_imagen, descripcion)
        if (count == 0):
            sys.exit(0)
        count -= 1


def avg_feature_vector(sentence, model, num_features, index2word_set):
    words = sentence.split()
    feature_vec = np.zeros((num_features, ), dtype='float32')
    n_words = 0
    for word in words:
        if word in index2word_set:
            n_words += 1
            feature_vec = np.add(feature_vec, model[word])
    if (n_words > 0):
        feature_vec = np.divide(feature_vec, n_words)
    return feature_vec