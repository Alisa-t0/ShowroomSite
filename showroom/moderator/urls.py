from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_moderator_main_page, name='moderator_main_page'),
    path('workers/', views.show_workers_list, name='workers_list'),
    path('cars/', views.show_cars_list, name='cars_list'),
    path('sales/', views.show_sales_list, name='sales_list'),
    path('workers/create', views.create_worker, name='create_worker'),
    path('cars/create', views.create_car, name='create_car'),
    path('sales/create', views.create_sale, name='create_sale'),
]