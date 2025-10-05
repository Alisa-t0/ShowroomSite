from django.shortcuts import render


from .models import Worker, Car

def show_main_page(request):
    return render(request, 'main/main_page.html')

def show_cars(request):
    cars = Car.objects.filter(is_available=True)
    return render(request, 'main/cars.html', {'cars': cars})

def show_workers(request):
    workers = Worker.objects.filter(is_active=True)
    return render(request, 'main/workers.html', {'workers': workers})

def show_contacts(request):
    return render(request, 'main/contacts.html')