# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Car(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.TextField()
    price = models.PositiveIntegerField()
    manufactDate = models.CharField(max_length=100)
    available = models.PositiveIntegerField()
    thumb = models.ImageField(default='rio_img.png',blank=True)

    def __str__(self):
        return self.name

    def getSnippet(self):
        return self.description[:50] + "..."
