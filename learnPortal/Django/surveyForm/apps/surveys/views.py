# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, 'surveys/index.html')

def process(request):
    if 'count' not in request.session:
        request.session['count']=0
    if request.method == 'POST':
        request.session['count']+=1
        request.session['name']=request.POST['name']
        request.session['loc']=request.POST['location']
        request.session['lang']=request.POST['language']
        request.session['com']=request.POST['comment']
    return redirect('/result')

def result(request):
    return render(request, 'surveys/result.html')
