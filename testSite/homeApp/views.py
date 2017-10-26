# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from common.stringsDir import strings

def home(request):
    return render(request, 'homeApp/home.html')
# Create your views here.
def navbar(request):
    language = "he"
    request.session.lang = "he"
    context = {
        'strings' : strings.getNebBarCon(language)
    }
    return render(request, 'homeApp/navbar.html', context)