from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_main_page, name='main_page'),
    path('cars', views.show_cars, name='cars_page'),
    path('workers', views.show_workers, name='workers_page'),
    path('contacts', views.show_contacts, name='contacts_page'),
]