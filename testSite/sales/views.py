# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from common.stringsDir import strings
from django.utils import translation
from django.http import HttpResponse

# Create your views here.
def sales(request):
    # language = translation.get_language_from_request(request)
    # translation.activate(language)
    # request.LANGUAGE_CODE = translation.get_language()
    language = request.LANGUAGE_CODE
    request.session.lang = language
    context = {}
    return render(request, 'sales/sales.html', context)

