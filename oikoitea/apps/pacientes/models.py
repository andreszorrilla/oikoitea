from django.db import models
from django.urls import reverse
from datetime import date
import random


class Paciente(models.Model):
    nombres     		= models.CharField(max_length=20, default="")
    apellidos   		= models.CharField(max_length=20, default="")
    fecha_nacimiento    = models.DateField(default=date.today())

    OPCIONES = (
        ('', ''),
        ('m', 'Masculino'),
        ('f', 'Femenino')
    )
    sexo = models.CharField('Sexo', choices=OPCIONES, default='', max_length=8)

    def get_edad(self):
        return (date.today() - self.fecha_nacimiento).days / 365


    def get_image_url(self):
        num = str(random.randint(1, 4))
        if (self.sexo == 'f'): return 'images/pacientes/girl-0' + num + '.png'
        return 'images/pacientes/boy-0' + num + '.png'
    
    def __str__(self):
        return self.nombres + " " + self.apellidos

    def get_full_name(self):
        return self.nombres + " " + self.apellidos

    def get_absolute_url(self):
        return reverse('paciente:paciente_index')

    def get_update_url(self):
        return reverse("paciente:paciente_edit", args=[self.pk])

    def get_delete_url(self):
        return reverse('paciente:paciente_index')

    @models.permalink
    def get_success_url(self):
        return reverse('paciente:paciente_index')
