# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from forms import SignUpForm

from common.stringsDir import strings
from django.http import HttpResponseRedirect
from django.views.generic import FormView
import datetime
from django.urls import reverse
#
# # class ColorStudyView(FormView):
# #     template_name = 'en/'
# #     form_class = PersonDetailForm
# #     success_url = '/'
#
def signup(request):
    language = request.LANGUAGE_CODE
    request.session.lang = language
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        signUpform = SignUpForm(request.POST)

        # Check if the form is valid:
        if signUpform.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            # test = form.cleaned_data['renewal_date']

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('home'))

    # If this is a GET (or any other method) create the default form.
    else:
        signUpform = SignUpForm({})


    return render(request, 'userControlApp/signup.html', { 'signUpform': signUpform })
# def signup(request):
#     return HttpResponse("Your prefs: %s\n\n\n\n%s \n\n\n\n %s" % request.META, request.session, request.path_info)
def login(request):
    return HttpResponse("Your prefs: %s\n\n\n\n%s \n\n\n\n %s" % request.META, request.session, request.path_info)
