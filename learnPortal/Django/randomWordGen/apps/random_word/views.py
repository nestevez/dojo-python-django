# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.crypto import get_random_string
from django.shortcuts import render, redirect

def index(request):
    if request.method == 'POST':
        request.session['randword']=get_random_string(length=14)
    elif 'randword' not in request.session:
        request.session['randword']=''
    if 'attemptct' not in request.session:
        request.session['attemptct']=0
    else:
        request.session['attemptct']+=1
    return render(request,'random_word/index.html')

def reset(request):
    request.session.clear()
    return redirect('/random_word/')
