# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from common.stringsDir import strings
from django.http import HttpResponse

# Create your views here.
def setPrefs(request):

    request.session.lang = "en"
    context = {
    }
    return HttpResponse("Your prefs: %s\n\n\n\n%s \n\n\n\n %s" % request.META , request.session , request.path_info)
    return render(request, prefs, context)
# Create your views here.
