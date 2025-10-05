from django.shortcuts import render

def show_main_page(request):
    return render(request, 'main/main_page.html')

def show_cars(request):
    return render(request, 'main/cars.html')

def show_workers(request):
    return render(request, 'main/workers.html')

def show_contacts(request):
    return render(request, 'main/contacts.html')