# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from cars import models as carModels
from .models import Rent
# Create your views here.

def add_rent(request):
    if request.method == 'POST':
        if 'carModel' in request.POST:
            rent = Rent()
            temp_car = carModels.Car.objects.get(slug=request.POST.get('carModel'))
            temp_car.available = temp_car.available - 1
            temp_car.save()
            rent.car = temp_car
            rent.client = request.user
            rent.status = "Unconfirmed"
            rent.save()
        return render(request, 'rents/addedRent.html')

def list_rents(request):
    rents = Rent.objects.all().order_by('id')
    if not request.user.is_staff:
        rents = [item for item in rents if request.user == item.client]
    return render(request, 'rents/list_rents.html', {'rents':rents})

def rent_details(request,id):
    rent = Rent.objects.get(id=id)
    return render(request, 'rents/rent_details.html', {'rent':rent})

def modify_rent(request):
    if request.method == 'POST':
        rent = Rent.objects.get(id=request.POST.get('rent_id'))
        rent.status = request.POST.get('current_status')
        rent.save()
    return redirect('rents:list')
