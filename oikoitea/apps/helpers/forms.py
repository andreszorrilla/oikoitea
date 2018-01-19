from crispy_forms.helper import FormHelper

class FormHelperHorizontal(FormHelper):
    def __init__(self, *args, **kwargs):
        super(FormHelperHorizontal, self).__init__(*args, **kwargs)
        self.form_tag = False
        self.label_class = 'col-md-2'
        self.field_class = 'col-md-4'