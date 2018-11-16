# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Presentation(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=200)
    image = models.ImageField(blank=True, null=True, default='')
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.name
