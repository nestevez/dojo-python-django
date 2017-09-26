# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .forms import *

# Create your views here.
def display(request):
    return render('survey/index.html')

def subreg(request):
    if request.method = "post":
        regform = Regform(request.POST)
        if regform.is_valid():
            return redirect('/users/')
        else:
            return redirect('/')
        else:
            return redirect('/')
