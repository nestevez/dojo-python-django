# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

# Create your views here.
def new_user(request):
    return render(request,'users/new.html')

def edit_prof(request):
    return render(request, 'users/edit.html')

def wall(request, user_id):
    context = {
    'num' : user_id,
    }
    print context['num']
    return render(request, 'users/show.html', context)

def edit_user(request):
    return render(request, 'users/edit.html')
