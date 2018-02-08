from django import forms
from django.utils.translation import ugettext_lazy as ugettext
from common.stringsDir import strings
import datetime
from crispy_forms.bootstrap import Tab, TabHolder
from crispy_forms.layout import Submit, Layout
from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, Fieldset
from django.urls import reverse
from django.core.validators import RegexValidator

class SignUpForm(forms.Form):
   #location = forms.CharField(required=True)
   first_name = forms.CharField(required=True, max_length=255, widget=forms.TextInput(attrs={'id':'off'}), initial={'name': 'instance2', 'id': 'test'})
   last_name = forms.CharField(required=True, max_length=255)
   email_regex = RegexValidator(regex=r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)',
                                message="Invalid email")
   email =  forms.CharField(validators=[email_regex], max_length=255, required=True)  # validators should be a list
   phone_regex = RegexValidator(regex=r'^\d{10}$',
                                message="Invalid phone number")
   phone = forms.CharField(validators=[phone_regex], max_length=11, required=False)  # validators should be a list
   #phone = forms.RegexField(regex=r'^\d{10}$', required=False)

   more_info = forms.CharField(required=False, max_length=1000, widget=forms.Textarea())
   terms_and_conditions = forms.BooleanField()

   def __init__(self, *args, **kwargs):
       super(SignUpForm, self).__init__(*args, **kwargs)
       self.helper = FormHelper()
       self.helper.form_id = 'id-personal-data-form'
       self.helper.form_method = 'post'
       #self.helper.form_action = reverse('navbar')
       self.helper.add_input(Submit('submit', 'Submit', css_class='btn-success'))
       self.helper.form_class = 'form-horizontal'
       self.helper.layout = Layout(
           #Fieldset('location', Field('location' ,placeHolder='Enter location', id='autocomplete', onFocus="geolocate()"), placeHolder='Enter location', css_id='test '),

                    Field('first_name', placeholder='Your first name',
                          css_class="some-class"),
                    Field('terms_and_conditions'),
                    Div('last_name', title="Your last name"),
           Fieldset('Contact data', 'email', 'phone'),

           TabHolder(Tab('About you', 'more_info')),

       )