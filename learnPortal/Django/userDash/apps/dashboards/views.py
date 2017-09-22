# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from ..logregs.models import * 


# Create your views here.
def index(request):
    context ={
    'user_level': "User",
    'users': Users.objects.all(),
    }
    return render(request, 'dashboards/dash.html', context)

def admin(request):
    context ={
    'user_level': "Manager",
    'users': Users.objects.all(),
    }
    return render(request, 'dashboards/dash.html', context)
