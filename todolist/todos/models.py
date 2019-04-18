# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from django.core.urlresolvers import reverse

class Todo(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    email = models.EmailField(null = True , blank = True)
    city = models.TextField(null = True)
    date = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
