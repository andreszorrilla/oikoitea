from crispy_forms.bootstrap import *
from crispy_forms.layout import Layout, Field
from django import forms
from django.contrib.auth.models import Group
from .models import Paciente

from crispy_forms.helper import FormHelper


class FormHelperHorizontal(FormHelper):
    def __init__(self, *args, **kwargs):
        super(FormHelperHorizontal, self).__init__(*args, **kwargs)
        self.form_tag = False
        self.label_class = 'col-md-2'
        self.field_class = 'col-md-4'


class PacienteForm(forms.ModelForm):

    helper = FormHelperHorizontal()

    use_required_attribute = False
    
    helper.layout = Layout(
        Field('nombres'),
        Field('apellidos'),
        AppendedText('fecha_nacimiento',
                    '<span class="glyphicon glyphicon-calendar" id="fecha_ingreso_datepicker"></span>',
                    autocomplete=False
                    ),
        Field('sexo'),
    )

    class Meta:
        model = Paciente
        fields = ['nombres', 'apellidos', 'fecha_nacimiento', 'sexo']