#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import logging
import re
import gensim
import sys

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from apps.fotos.models import Foto, DescripcionFoto


logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def format_name(self, name):
        nombre_formateado = re.sub("_\d*", "", name)
        nombre_formateado = re.sub("\.\/", "", nombre_formateado)
        nombre_formateado = re.sub("\.(jpg|png)", "", nombre_formateado)
        return nombre_formateado


    def handle(self, *args, **options):
        descripciones_fotos = DescripcionFoto.objects.all()

        count = 0
        total = len(descripciones_fotos)

        for descripcion in descripciones_fotos:
            descripcion.descripcion_fake = descripcion.descripcion
            descripcion.save()

            print count, " de ", total
            count = count + 1



