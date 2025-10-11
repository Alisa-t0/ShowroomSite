from django.urls import path
from . import views

urlpatterns = [
    path('main_page', views.show_moderator_main_page, name='moderator_main_page'),
    path('login', views.show_login_page_moderator, name='login_moderator'),
    path('workers/', views.show_workers_list, name='workers_list'),
    path('cars/', views.show_cars_list, name='cars_list'),
    path('sales/', views.show_sales_list, name='sales_list'),
    path('workers/create', views.create_worker, name='create_worker'),
    path('cars/create', views.create_car, name='create_car'),
    path('sales/create', views.create_sale, name='create_sale'),
    path('workers/<int:pk>', views.WorkerDetailView.as_view(), name='worker_details'),
    path('workers/<int:pk>/update', views.WorkerUpdateView.as_view(), name='worker_update'),
    path('workers/<int:pk>/delete', views.WorkerDeleteView.as_view(), name='worker_delete'),
    path('cars/<int:pk>', views.CarDetailView.as_view(), name='car_details'),
    path('cars/<int:pk>/update', views.CarUpdateView.as_view(), name='car_update'),
    path('cars/<int:pk>/delete', views.CarDeleteView.as_view(), name='car_delete'),
    path('sales/<int:pk>', views.SaleDetailView.as_view(), name='sale_details'),
    path('sales/<int:pk>/update', views.SaleUpdateView.as_view(), name='sale_update'),
    path('sales/<int:pk>/delete', views.SaleDeleteView.as_view(), name='sale_delete'),
    path('reports', views.show_reports, name='reports'),
    path('logout_moderator', views.logout_moderator, name='logout_moderator'),
]