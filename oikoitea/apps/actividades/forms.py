from crispy_forms.bootstrap import *
from crispy_forms.layout import Layout, Field
from django import forms
from .models import Actividad, ActividadDetalle

from crispy_forms.helper import FormHelper
from django.forms.formsets import BaseFormSet


class FormHelperHorizontal(FormHelper):
    def __init__(self, *args, **kwargs):
        super(FormHelperHorizontal, self).__init__(*args, **kwargs)
        self.form_tag = False
        self.label_class = 'col-md-2'
        self.field_class = 'col-md-4'


class ActividadDetalleForm(forms.ModelForm):

    """
    Formulario para fotografias y descripciones de plantilla de agenda.
    """
    
    helper = FormHelper()
    use_required_attribute = False
    helper.layout = Layout(
        Field('imagen'),
        Field('descripcion'),
        Field('img_url'),
        Field('foto'),
    )
    class Meta:
        model = ActividadDetalle
        fields = ('imagen', 'descripcion', 'img_url', 'foto')


class ActividadForm(forms.ModelForm):

    """
    Formulario para encabezado de la agenda.
    """

    helper = FormHelper()

    use_required_attribute = False
    
    helper.layout = Layout(
        Field('nombre'),
        Field('descripcion'),
    )

    class Meta:
        model = Actividad
        fields = ['nombre', 'descripcion']





class BaseLinkFormSet(BaseFormSet):
    def clean(self):
        """
        Adds validation to check that no two links have the same anchor or URL
        and that all links have both an anchor and URL.
        """
        if any(self.errors):
            return

        anchors = []
        urls = []
        duplicates = False

        for form in self.forms:
            if form.cleaned_data:
                anchor = form.cleaned_data['descripcion']
                url = form.cleaned_data['url']

                # Check that no two links have the same anchor or URL
                #    if anchor and url:
                #        if anchor in anchors:
                #            duplicates = True
                #        anchors.append(anchor)
                #        if url in urls:
                #            duplicates = True
                #        urls.append(url)
                #    if duplicates:
                #        raise forms.ValidationError(
                #            'Links must have unique anchors and URLs.',
                #            code='duplicate_links'
                #        )
                #    # Check that all links have both an anchor and URL
                #    if url and not anchor:
                #        raise forms.ValidationError(
                #            'All links must have an anchor.',
                #            code='missing_anchor'
                #        )
                #    elif anchor and not url:
                #        raise forms.ValidationError(
                #            'All links must have a URL.',
                #            code='missing_URL'
                #        )