from django.shortcuts import render

import logging

from .models import Worker, Car

logger = logging.getLogger('main')

def show_main_page(request):
    logger.info('Користувач перейшов на головну сторінку сайту.')
    return render(request, 'main/main_page.html')

def show_cars(request):
    logger.info(f'Користувач переглянув сторінку з доступними авто.')
    cars = Car.objects.filter(is_available=True)
    return render(request, 'main/cars.html', {'cars': cars})

def show_workers(request):
    logger.info(f'Користувач переглянув сторінку працівників.')
    workers = Worker.objects.filter(is_active=True)
    return render(request, 'main/workers.html', {'workers': workers})

def show_contacts(request):
    logger.info('Користувач відкрив сторінку контактів.')
    return render(request, 'main/contacts.html')