from django import forms
from django.forms.fields import Field
from .models import Register

my_custom_errors = {
    'required': 'Este campo es requerido',
    'invalid': 'Este campo es inválido'
}


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ('name','last_name','dni','school_name','email','year_in_school')

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        '''for field in self.fields:
            if 'required' in self.fields[field].error_messages:
                self.fields[field].error_messages['required'] = 'Este campo debe ser llenado.'
            if 'invalid' in self.fields[field].default_error_messages:
                self.fields.Field[field].default_error_messages['invalid'] = 'Este campo es inválido.'''

        # add custom error messages
        self.fields['name'].error_messages = my_custom_errors
        self.fields['last_name'].error_messages = my_custom_errors
        self.fields['dni'].error_messages = my_custom_errors
        self.fields['school_name'].error_messages = my_custom_errors
        self.fields['email'].error_messages = my_custom_errors
        self.fields['year_in_school'].error_messages = my_custom_errors

class ContactForm(forms.Form):
    #name = forms.CharField(max_length=255)
    subject = forms.CharField(required=True,max_length=200,error_messages=my_custom_errors)
    from_email = forms.EmailField(required=True,error_messages=my_custom_errors)
    message = forms.CharField(widget=forms.Textarea,error_messages=my_custom_errors)
