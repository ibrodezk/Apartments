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

class Test(forms.Form):
    searchSales = forms.CharField(label='searchSales', max_length=100)
    renewal_date = forms.DateField(help_text=strings.getFormSearchSales()["date_help_text"], localize=True)

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        # Check date is not in past.
        if data < datetime.date.today():
            raise ValidationError(ugettext('Invalid date - renewal in past'))

        # Check date is in range librarian allowed to change (+4 weeks).
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(ugettext('Invalid date - renewal more than 4 weeks ahead'))

        # Remember to always return the cleaned data.
        return data

    def test(self):
        return self.searchSales;

class NoFormTagCrispyFormMixin(object):
    @property
    def helper(self):
        if not hasattr(self, '_helper'):
            self._helper = FormHelper()
            self._helper.form_tag = False
        return self._helper


# class PersonDetailForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     age = forms.IntegerField(required=False)
#     address1 = forms.CharField(max_length=50, required=False)
#     address2 = forms.CharField(max_length=50, required=False)
#     city = forms.CharField(max_length=50, required=False)
#     state = forms.CharField(max_length=50, required=False)
#
#     mobile = forms.CharField(max_length=32, required=False)
#     home = forms.CharField(max_length=32, required=False)
#     office = forms.CharField(max_length=32, required=False)
#     twitter = forms.CharField(max_length=100, required=False)
#
#     def __init__(self, *args, **kwargs):
#         super(PersonDetailForm, self ).__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_tag = False
#         self.helper.layout = Layout(
#             TabHolder(
#                 Tab('Information',
#                     'name',
#                     'age'
#                     ),
#                 Tab('Address',
#                     'address1',
#                     'address2',
#                     'city',
#                     'state'
#                 ),
#                 Tab('Contact',
#                     'mobile',
#                     'home',
#                     'office',
#                     'twitter',
#                 )
#             )
#         )
#         self.helper.layout.append(Submit('submit', 'Submit'))
class SalesSearchForm(forms.Form):
   location = forms.CharField(required=True)
   first_name = forms.CharField(required=True, max_length=255, widget=forms.TextInput(attrs={'id':'off'}), initial={'name': 'instance2', 'id': 'test'})
   last_name = forms.CharField(required=True, max_length=255)
   email = forms.EmailField(required=True)
   phone = forms.CharField(required=True, max_length=200)
   address = forms.CharField(max_length=1000, widget=forms.Textarea())
   more_info = forms.CharField(max_length=1000, widget=forms.Textarea())
   color = forms.TypedChoiceField(
       label="Choose color",
       choices=((0, "Red"), (1, "Blue"), (2, "Green")),
       coerce=lambda x: bool(int(x)),
       widget=forms.RadioSelect,
       initial='0',
       required=True)

   def __init__(self, *args, **kwargs):
       super(SalesSearchForm, self).__init__(*args, **kwargs)
       self.helper = FormHelper()
       self.helper.form_id = 'id-personal-data-form'
       self.helper.form_method = 'post'
       self.helper.form_action = reverse('navbar')
       self.helper.add_input(Submit('submit', 'Submit', css_class='btn-success'))
       self.helper.form_class = 'form-horizontal'
       self.helper.layout = Layout(
           Fieldset('location', Field('location' ,placeHolder='Enter location', id='autocomplete', onFocus="geolocate()"), placeHolder='Enter location', css_id='test '),
           Fieldset('Name',
                    Field('first_name', placeholder='Your first name',
                          css_class="some-class"),
                    Div('last_name', title="Your last name"),),
           Fieldset('Contact data', 'email', 'phone', style="color: brown;"),
           InlineRadios('color'),
           TabHolder(Tab('Address', 'address'),
                     Tab('More Info', 'more_info')))