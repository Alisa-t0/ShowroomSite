from django.forms import ModelForm, TextInput, NumberInput, CheckboxInput, DateInput, Select
from main.models import Worker, Car, Sale

class WorkerForm(ModelForm):
    class Meta:
        model = Worker
        fields = ['full_name', 'position', 'phone', 'email', 'is_active']
        labels = {
            'full_name': 'ПІБ',
            'position': 'Посада',
            'phone': 'Телефон',
            'email': 'Email',
            'is_active': 'Активний',
        }
        widgets = {
            'full_name': TextInput(attrs={'class': 'form-control'}),
            'position': TextInput(attrs={'class': 'form-control'}),
            'phone': TextInput(attrs={'class': 'form-control'}),
            'email': TextInput(attrs={'class': 'form-control'}),
            'is_active': CheckboxInput(attrs={'class': 'form-check-input'})
        }

class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ['producer_name', 'year_production', 'model', 'cost','potential_selling_price','is_available']
        labels = {
            'producer_name': 'Назва виробника',
            'year_production': 'Рік випуску',
            'model': 'Модель',
            'cost': 'Собівартість',
            'potential_selling_price': 'Потенційна ціна продажу',
            'is_available': 'Наявна в салоні',
        }
        widgets = {
            'producer_name': TextInput(attrs={'class': 'form-control'}),
            'year_production': NumberInput(attrs={'class': 'form-control'}),
            'model': TextInput(attrs={'class': 'form-control'}),
            'cost': NumberInput(attrs={'class': 'form-control'}),
            'potential_selling_price': NumberInput(attrs={'class': 'form-control'}),
            'is_available': CheckboxInput(attrs={'class': 'form-check-input'})
        }

class SaleForm(ModelForm):
    class Meta:
        model = Sale
        fields = ['worker', 'car', 'sale_date', 'selling_price']
        labels = {
            'worker': 'Працівник',
            'car': 'Машина',
            'sale_date': 'Дата продажу',
            'selling_price': 'Реальна ціна продажу',
        }
        widgets = {
            'worker': Select(attrs={'class': 'form-control'}),
            'car': Select(attrs={'class': 'form-control'}),
            'sale_date': DateInput(attrs={'class': 'form-control','type':'date'}),
            'selling_price': NumberInput(attrs={'class': 'form-control'}),
        }