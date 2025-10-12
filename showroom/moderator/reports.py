from main.models import Worker, Car, Sale

def all_workers():
    return Worker.objects.all()

def all_cars():
    return Car.objects.all()

def all_sales():
    return Sale.objects.all()

def sales_by_date(date):
    return Sale.objects.filter(sale_date=date)

def sales_by_time_period(start_date, end_date):
    return Sale.objects.filter(sale_date__range=(start_date, end_date))

def sales_by_worker(worker_id):
    return Sale.objects.filter(worker=worker_id), worker_id

def bestseller_car_by_time_period(start_date, end_date):
    bestseller_car = None
    count_bestseller_car = 0
    for sale in sales_by_time_period(start_date, end_date):
        count_car = Sale.objects.filter(car__producer_name=sale.car.producer_name, car__model=sale.car.model).count()
        if count_car > count_bestseller_car:
            count_bestseller_car = count_car
            bestseller_car = sale.car

    return Sale.objects.filter(car__producer_name=sale.car.producer_name, car__model=sale.car.model), bestseller_car, count_bestseller_car

def top_seller_by_time_period(start_date, end_date):
    top_seller = None
    profit_top_seller = 0
    for sale in sales_by_time_period(start_date, end_date):
        worker_sales = Sale.objects.filter(worker=sale.worker)
        profit_worker = 0
        for worker_sale in worker_sales:
            profit_worker += worker_sale.profit
        if profit_worker > profit_top_seller:
            profit_top_seller = profit_worker
            top_seller = sale.worker
    return Sale.objects.filter(worker=top_seller), top_seller, profit_top_seller

def total_profit_by_time_period(start_date, end_date):
    total_profit = 0
    for sale in sales_by_time_period(start_date, end_date):
        total_profit += sale.profit

    return sales_by_time_period(start_date, end_date),total_profit


