# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Car
from django.http import HttpResponse
# Create your views here.

def car_list(request):
    if request.method == 'POST':
        if request.POST.get('filter') == "price":
            cars = Car.objects.all().order_by('name')
        else:
            cars = Car.objects.all().order_by('name')
    else:
        cars = Car.objects.all().order_by('name')
    cars = [item for item in cars if item.available > 0]
    return render(request, 'cars/car_list.html', {'cars': cars})

def car_detail(request, slug):
    # return HttpResponse(slug)
    car = Car.objects.get(slug=slug)
    return render(request, 'cars/car_detail.html', {'car':car})
