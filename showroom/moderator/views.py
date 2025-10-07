from django.shortcuts import render, redirect
from main.models import Worker, Car, Sale
from .forms import WorkerForm, CarForm, SaleForm
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

def create_object(request, object_form, object_name, redirect_url):
    if request.method == 'POST':
        form = object_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(redirect_url)
    else:
        form = object_form()
    return render(request, 'moderator/create_object.html', {'form': form, 'object_name': object_name})

def create_worker(request):
    return create_object(request,
        object_form=WorkerForm,
        object_name='працівника',
        redirect_url='workers_list'
    )


def create_car(request):
    return create_object(
        request,
        object_form=CarForm,
        object_name='машину',
        redirect_url='cars_list'
    )


def create_sale(request):
    return create_object(
        request,
        object_form=SaleForm,
        object_name='продаж',
        redirect_url='sales_list'
    )
