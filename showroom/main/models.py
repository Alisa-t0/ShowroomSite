from django.db import models

# Create your models here.
class Worker(models.Model):
    full_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return f'/moderator/workers/{self.pk}'

class Car(models.Model):
    producer_name = models.CharField(max_length=100)
    year_production = models.IntegerField()
    model = models.CharField(max_length=100)
    cost = models.IntegerField()
    potential_selling_price = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.producer_name} {self.model}'

    def get_absolute_url(self):
        return f'/moderator/cars/{self.pk}'

class Sale(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.PROTECT)
    car = models.ForeignKey(Car, on_delete=models.PROTECT)
    sale_date = models.DateField()
    selling_price = models.IntegerField()
    profit = models.IntegerField(editable=False, default=0)

    def __str__(self):
        return f'Продаж: {self.car.producer_name} {self.car.model} з {self.worker.full_name}'

    def get_absolute_url(self):
        return f'/moderator/sales/{self.pk}'

    def save(self, *args, **kwargs):
        self.profit = self.selling_price - self.car.cost
        super().save(*args, **kwargs)
