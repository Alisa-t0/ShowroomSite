from django.db import models

# Create your models here.
class Worker(models.Model):
    full_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    is_active = models.BooleanField(default=True)

class Car(models.Model):
    producer_name = models.CharField(max_length=100)
    year_production = models.IntegerField()
    model = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    potential_selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

class Sale(models.Model):
    employee = models.ForeignKey(Worker, on_delete=models.PROTECT)
    car = models.ForeignKey(Car, on_delete=models.PROTECT)
    sale_date = models.DateField()
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)


