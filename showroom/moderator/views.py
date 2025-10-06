from django.shortcuts import render
from main.models import Worker, Car, Sale
# Create your views here.
def show_moderator_main_page(request):
    return render(request, 'moderator/moderator_main_page.html')

def show_workers_list(request):
    all_workers = Worker.objects.all()
    return render(request, 'moderator/workers/workers_list.html', {'all_workers': all_workers})

def show_cars_list(request):
    all_cars = Car.objects.all()
    return render(request, 'moderator/cars/cars_list.html', {'all_cars': all_cars})

def show_sales_list(request):
    all_sales = Sale.objects.all()
    return render(request, 'moderator/sales/sales_list.html', {'all_sales': all_sales})