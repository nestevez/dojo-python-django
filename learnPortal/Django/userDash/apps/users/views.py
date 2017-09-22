# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from ..logregs.models import *
from .models import *
from .forms import *

# Create your views here.
def new_user(request):
    return render(request,'users/new.html')

def edit_prof(request):
    return render(request, 'users/edit.html')

def wall(request, user_id):
    context = {
    'user': Users.objects.get(id=user_id),
    'num' : user_id,
    'form': msg_form,
    }
    print context['user']
    return render(request, 'users/show.html', context)

def msg(request):
    return redirect(reverse('users:user_info'))

def edit_user(request):
    return render(request, 'users/edit.html')
