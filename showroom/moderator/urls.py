from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_moderator_main_page, name='moderator_main_page'),
]