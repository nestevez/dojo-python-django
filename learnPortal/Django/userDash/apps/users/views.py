# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import *
from .forms import *

# Create your views here.
def new_user(request):
    return render(request,'users/new.html')

def edit_prof(request):
    context = {
    'detail_form': edit_user,
    'pw_form': edit_pw,
    'desc_form': msg_form,
    }
    return render(request, 'users/edit.html', context)

def edit_user(request):
    context = {
    'detail_form': edit_user,
    'pw_form': edit_pw,
    'desc_form': msg_form,
    }
    return render(request, 'users/edit.html', context)

def submit_edit(request):
    data = request.POST
    errors = Users.objects.detail_check(data)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect(reverse('users:edit_user', kwargs={'user_id':}))
    else:
    return redirect(reverse('users:user_info', kwargs={'user_id':})

def wall(request, user_id):
    usr = Users.objects.get(id=user_id)
    context = {
    'user': usr,
    'num' : user_id,
    'form': msg_form,
    'mssgs': Mssgs.objects.filter(to_user=usr),
    }
    return render(request, 'users/show.html', context)

def msg(request):
    mess = request.POST
    frm = Users.objects.get(email=request.session['usr'])
    touser = Users.objects.get(id=mess['to_user'])
    Mssgs.objects.create(msg=mess['msg'], from_user=frm, to_user=touser)
    ##error here!!!!
    return redirect(reverse('users:user_info', kwargs={'user_id': mess['to_user']})
