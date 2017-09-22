# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    if 'words' not in request.session:
        request.session['words']=[]
    return render(request,'session_words/index.html')

def add(request):
    if request.method == 'POST':
        word=request.POST['word']
        color=request.POST['color']
        big=request.POST['big']
        print request.POST['big']
        classes = ''
        if big is on:
            classes += 'big '
        if color:
            classes += str(color)
        request.session['words'].append('<p class="{}">{}</p> - added on (date)'.format(classes, word))
    return redirect('/session_words/')


def clear(request):
    request.session.clear()
    return redirect('/session_words/')
