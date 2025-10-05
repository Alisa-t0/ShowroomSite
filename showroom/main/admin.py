from django.contrib import admin
from .models import Worker, Car, Sale
# Register your models here.
admin.site.register(Car)
admin.site.register(Worker)
admin.site.register(Sale)