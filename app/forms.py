from .models import *
from django.forms import ModelForm
from django import forms

class writingForm(ModelForm):
    class Meta:
        model = WritingModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(writingForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Your Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Your Email address'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Your Phone number'

class newsletterForm(ModelForm):
    class Meta:
        model = newsletter
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(newsletterForm, self).__init__(*args, **kwargs)
        self.fields['newsletter_field'].widget.attrs['placeholder'] = 'Enter Your Email'