# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
class Userstest(models.Model):
    username = models.CharField(max_length=255)
    location = models.SlugField(unique=True, max_length=255)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.TextField()
# Create your models here.
