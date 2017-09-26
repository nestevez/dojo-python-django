# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from .forms import Signin_Form, Reg_Form
from .models import *

# Create your views here.
def index(request):
    return render(request, 'logregs/home.html')

def signin(request):
    context = {
    'form': Signin_Form,
    }
    return render(request, 'logregs/signin.html', context)

def register(request):
    context = {
    'form': Reg_Form,
    }
    return render(request, 'logregs/register.html', context)

def validreg(request):
    data = request.POST
    errors = Users.objects.users_valid(data)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect(reverse('logregs:reg'))
    else:
        pwhash = bcrypt.hashpw(data['pw'].encode(), bcrypt.gensalt())
        Users.objects.create(fname=data['fname'], lname=data['lname'],email=data['email'], pw=pwhash)
        request.session['usr']=data['email']
        request.session['action']='registered'
        return redirect('dash:user_dashboard')

def validlog(request):
    data = request.POST
    errors = Users.objects.login_valid(data)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect(reverse('logregs:signin'))
    else:
        request.session['usr'] = data['email']
        request.session['action']='logged in'
        return redirect('dash:user_dashboard')
