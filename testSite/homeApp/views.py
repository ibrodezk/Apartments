# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from common.stringsDir import strings
from forms import Test, SalesSearchForm
from django.http import HttpResponseRedirect
from django.views.generic import FormView
import datetime
from django.urls import reverse

# class ColorStudyView(FormView):
#     template_name = 'en/'
#     form_class = PersonDetailForm
#     success_url = '/'

def navbar(request):
    language = request.LANGUAGE_CODE
    request.session.lang = language
    context = {}
    return render(request, 'homeApp/navbar.html', context)

def home(request):
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = Test(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            test = form.cleaned_data['renewal_date']

            # redirect to a new URL:
            return HttpResponseRedirect(reverse(''))

    # If this is a GET (or any other method) create the default form.
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = Test(initial={'renewal_date': proposed_renewal_date,})
        salesForm = SalesSearchForm({});

    return render(request, 'homeApp/home.html', { 'form': form ,'salesForm': salesForm})