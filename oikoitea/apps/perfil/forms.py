from django.contrib.auth.models import User
from django import forms
from .models import UserProfile
from django.core.files.images import get_image_dimensions

from crispy_forms.bootstrap import *
from crispy_forms.layout import Layout, Field
from django.contrib.auth.models import Group

from crispy_forms.helper import FormHelper


class FormHelperHorizontal(FormHelper):
    def __init__(self, *args, **kwargs):
        super(FormHelperHorizontal, self).__init__(*args, **kwargs)
        self.form_tag = False
        self.label_class = 'col-md-2'
        self.field_class = 'col-md-4'



class UpdateUserForm(forms.ModelForm):

    helper = FormHelperHorizontal()
    use_required_attribute = False

    helper.layout = Layout(
        Field('username'),
        Field('email'),
        Field('first_name'),
        Field('last_name'),
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']











class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('avatar',)
        exclude = ['user']

    def clean_avatar(self):
        avatar = self.cleaned_data['avatar']
        print( self.cleaned_data )

        try:
            w, h = get_image_dimensions(avatar)

            #validate dimensions
            max_width = max_height = 1000
            if w > max_width or h > max_height:
                raise forms.ValidationError(
                    u'Please use an image that is '
                     '%s x %s pixels or smaller.' % (max_width, max_height))

            #validate content type
            main, sub = avatar.content_type.split('/')
            if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
                raise forms.ValidationError(u'Please use a JPEG, '
                    'GIF or PNG image.')

            #validate file size
            if len(avatar) > (20 * 1024):
                raise forms.ValidationError(
                    u'Avatar file size may not exceed 20k.')

        except AttributeError:
            """
            Handles case when we are updating the user profile
            and do not supply a new avatar
            """
            pass

        return avatar