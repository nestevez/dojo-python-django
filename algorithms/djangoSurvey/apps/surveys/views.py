# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from .forms import Survey1

# Create your views here.
def index(request):
    context = {
        'form': Survey1()
    }
    return render(request, 'surveys/index.html', context)

def results(request):
    return render(request, 'surveys/results.html')

def submit(request):
    return redirect(reverse('form'))
