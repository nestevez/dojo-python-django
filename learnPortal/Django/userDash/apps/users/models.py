# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from ..logregs.models import *

# Create your models here.
class Messages(models.Model):
    msg = models.TextField()
    from_user = models.ForeignKey(Users, related_name="msgs_sent")
    to_user = models.ForeignKey(Users, related_name="msgs_received")
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now = True)
