import json
import os

from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView
from main.models import Worker, Car, Sale
from .forms import WorkerForm, CarForm, SaleForm
from datetime import datetime
from . import reports
from hashlib import sha256
from dotenv import load_dotenv
from .decorators import moderator_required
from django.http import HttpResponse

# Create your views here.
load_dotenv()

def show_login_page_moderator(request):
    error = None
    if request.method == 'POST':
        entered_login = sha256(request.POST.get('login', '').encode()).hexdigest()
        entered_password = sha256(request.POST.get('password', '').encode()).hexdigest()

        correct_login = os.getenv('MYSHOWROOM_LOGIN')
        correct_password = os.getenv('MYSHOWROOM_PASSWORD')
        if entered_login == correct_login and entered_password == correct_password:
            request.session['is_moderator'] = True
            return redirect('moderator_main_page')
        error = 'Невірні дані'
    return render(request, 'moderator/login_page.html', {'error': error})


def logout_moderator(request):
    request.session.pop('is_moderator', None)
    return redirect('main_page')


@moderator_required
def show_moderator_main_page(request):
    return render(request, 'moderator/moderator_main_page.html')

class CarDetailView(DetailView):
    model = Car
    template_name = 'moderator/cars/detail_view.html'
    context_object_name = 'car'

class WorkerDetailView(DetailView):
    model = Worker
    template_name = 'moderator/workers/detail_view.html'
    context_object_name = 'worker'

class SaleDetailView(DetailView):
    model = Sale
    template_name = 'moderator/sales/detail_view.html'
    context_object_name = 'sale'

class CarUpdateView(UpdateView):
    model = Car
    template_name = 'moderator/update.html'
    context_object_name = 'car'
    form_class = CarForm

class WorkerUpdateView(UpdateView):
    model = Worker
    template_name = 'moderator/update.html'
    context_object_name = 'worker'
    form_class = WorkerForm

class SaleUpdateView(UpdateView):
    model = Sale
    template_name = 'moderator/update.html'
    context_object_name = 'sale'
    form_class = SaleForm

class CarDeleteView(DeleteView):
    model = Car
    template_name = 'moderator/delete.html'
    context_object_name = 'car'
    success_url = '..'

class WorkerDeleteView(DeleteView):
    model = Worker
    template_name = 'moderator/delete.html'
    context_object_name = 'worker'
    success_url = '..'

class SaleDeleteView(DeleteView):
    model = Sale
    template_name = 'moderator/delete.html'
    context_object_name = 'sale'
    success_url = '..'

@moderator_required
def show_workers_list(request):
    all_workers = Worker.objects.all()
    return render(request, 'moderator/workers/workers_list.html', {'all_workers': all_workers})

@moderator_required
def show_cars_list(request):
    all_cars = Car.objects.all()
    return render(request, 'moderator/cars/cars_list.html', {'all_cars': all_cars})

@moderator_required
def show_sales_list(request):
    all_sales = Sale.objects.all()
    return render(request, 'moderator/sales/sales_list.html', {'all_sales': all_sales})

@moderator_required
def create_object(request, object_form, object_name, redirect_url):
    if request.method == 'POST':
        form = object_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(redirect_url)
    else:
        form = object_form()
    return render(request, 'moderator/create_object.html', {'form': form, 'object_name': object_name})

@moderator_required
def create_worker(request):
    return create_object(request,
                         object_form=WorkerForm,
                         object_name='працівника',
                         redirect_url='workers_list'
                         )

@moderator_required
def create_car(request):
    return create_object(
        request,
        object_form=CarForm,
        object_name='машину',
        redirect_url='cars_list'
    )

@moderator_required
def create_sale(request):
    return create_object(request,
        object_form=SaleForm,
        object_name='продаж',
        redirect_url='sales_list'
    )

@moderator_required
def show_reports(request):
    report_type = request.GET.get('report_type')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    worker_id = request.GET.get('worker_id')

    if start_date:
        start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
    if end_date:
        end_date = datetime.strptime(end_date, '%Y-%m-%d').date()

    data = None
    title = ''
    extra_info = {}
    template_name = 'moderator/sales/reports.html'
    workers_list = Worker.objects.all()
    if report_type == 'all_workers':
        data = Worker.objects.all()
        title = 'Повна інформація про співробітників'
        template_name = 'moderator/workers/reports.html'

    elif report_type == 'all_cars':
        data = Car.objects.all()
        title = 'Повна інформація про автомобілі'
        template_name = 'moderator/cars/reports.html'

    elif report_type == 'all_sales':
        data = Sale.objects.all()
        title = 'Повна інформація про продажі'

    elif report_type == 'sales_by_date' and start_date:
        data = reports.sales_by_date(start_date)
        title = f'Продажі за {start_date}'

    elif report_type == 'sales_by_time_period' and start_date and end_date:
        data = reports.sales_by_time_period(start_date, end_date)
        title = f'Продажі з {start_date} по {end_date}'

    elif report_type == 'sales_by_worker' and worker_id:
        data, worker_id = reports.sales_by_worker(worker_id)
        title = 'Продажі конкретного працівника'

    elif report_type == 'bestseller_car_by_time_period' and start_date and end_date:
        car, bestseller_car, count = reports.bestseller_car_by_time_period(start_date, end_date)
        data = car
        extra_info = {'count': count, 'car': bestseller_car}
        title = f'Найбільш продаваний автомобіль з {start_date} по {end_date}'

    elif report_type == 'top_seller_by_time_period' and start_date and end_date:
        worker, top_seller, profit = reports.top_seller_by_time_period(start_date, end_date)
        data = worker
        extra_info = {'worker_profit': profit, 'worker': top_seller}
        title = f'Найуспішніший продавець з {start_date} по {end_date}'

    elif report_type == 'total_profit_by_time_period' and start_date and end_date:
        sales, profit = reports.total_profit_by_time_period(start_date, end_date)
        data = sales
        extra_info = {'profit': profit}
        title = f'Сумарний прибуток з {start_date} по {end_date}'

    return render(request, template_name,{'data': data, 'title': title, 'extra_info': extra_info, 'workers_list': workers_list})

def export_sales(request):
    sales = Sale.objects.all()
    data = {
        'sales': [{
            'id': sale.id,
            'worker': sale.worker.full_name,
            'car': f'{sale.car.producer_name} {sale.car.model}',
            'sale_date': str(sale.sale_date),
            'selling_price': sale.selling_price,
            'profit': sale.profit,
            }for sale in sales
        ]
    }

    with open('sales.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    return render(request, 'moderator/export_done.html')


def export_cars(request):
    cars = Car.objects.all()
    data = {
        'cars': [{
            'id': car.id,
            'producer_name': car.producer_name,
            'year_production': car.year_production,
            'model': car.model,
            'cost': car.cost,
            'potential_selling_price': car.potential_selling_price,
            'is_available': car.is_available,
            }for car in cars
        ]
    }

    with open('cars.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    return render(request, 'moderator/export_done.html')


def export_workers(request):
    workers = Worker.objects.all()
    data = {
        'workers': [{
            'id': worker.id,
            'full_name': worker.full_name,
            'position': worker.position,
            'phone': worker.phone,
            'email': worker.email,
            'is_active': worker.is_active,
            }for worker in workers
        ]
    }
    with open('workers.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    return render(request, 'moderator/export_done.html')

def import_sales_from_file(request):
    try:
        with open('sales.json', 'r', encoding='utf-8-sig') as file:
            sales = json.load(file)
            for sale_data in sales.get('sales'):
                worker, _ = Worker.objects.get_or_create(full_name=sale_data['worker'])

                car_info = sale_data['car'].split(' ', 1)
                car, _ = Car.objects.get_or_create(producer_name=car_info[0], model=car_info[1])

                Sale.objects.get_or_create(
                    id=sale_data['id'],
                    defaults={
                        'worker': worker,
                        'car': car,
                        'sale_date': sale_data['sale_date'],
                        'selling_price': sale_data['selling_price'],
                        'profit': sale_data['profit']}
                )
            return render(request, 'moderator/import_done.html')
    except FileNotFoundError:
        return HttpResponse('<h4>Помилка. Файл не знайдено</h4>')
    except json.JSONDecodeError:
        return HttpResponse('<h4>Помилка. Файл не розпізнано</h4>')

def import_cars_from_file(request):
    try:
        with open('cars.json', 'r', encoding='utf-8-sig') as file:
            cars = json.load(file)
            for car_data in cars.get('cars'):
                Car.objects.get_or_create(
                    id=car_data['id'],
                    defaults={
                        'producer_name': car_data['producer_name'],
                        'year_production': car_data['year_production'],
                        'model': car_data['model'],
                        'cost': car_data['cost'],
                        'potential_selling_price': car_data['potential_selling_price'],
                        'is_available': car_data['is_available']}
                    )
            return render(request, 'moderator/import_done.html')
    except FileNotFoundError:
        return HttpResponse('<h4>Помилка. Файл не знайдено</h4>')
    except json.JSONDecodeError:
        return HttpResponse('<h4>Помилка. Файл не розпізнано</h4>')

def import_workers_from_file(request):
    try:
        with open('workers.json', 'r', encoding='utf-8-sig') as file:
            workers = json.load(file)
            for worker_data in workers.get('workers'):
                Worker.objects.get_or_create(
                    id=worker_data['id'],
                    defaults={
                            'full_name': worker_data['full_name'],
                            'position': worker_data['position'],
                            'phone': worker_data['phone'],
                            'email': worker_data['email'],
                            'is_active': worker_data['is_active'],
                    }
                 )
            return render(request, 'moderator/import_done.html')
    except FileNotFoundError:
        return HttpResponse('<h4>Помилка. Файл не знайдено</h4>')
    except json.JSONDecodeError:
        return HttpResponse('<h4>Помилка. Файл не розпізнано</h4>')
