# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from cars import models as carModels
# Create your models here.
import smtplib, ssl

class Rent(models.Model):
    client = models.ForeignKey(User, default=None)
    car = models.ForeignKey(carModels.Car, default=None)
    status = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    driver = models.CharField(max_length=50)
    delivered = models.CharField(max_length=50)
    adresa = models.CharField(max_length=50, default="None")
    def __str__(self):
        return str(self.id)
