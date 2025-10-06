from django.forms import ModelForm, TextInput, NumberInput, CheckboxInput, DateInput, Select
from main.models import Worker, Car, Sale

class WorkerForm(ModelForm):
    class Meta:
        model = Worker
        fields = ['full_name', 'position', 'phone', 'email', 'is_active']
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
        widgets = {
            'worker': Select(attrs={'class': 'form-control'}),
            'car': Select(attrs={'class': 'form-control'}),
            'sale_date': DateInput(attrs={'class': 'form-control','type':'date'}),
            'selling_price': NumberInput(attrs={'class': 'form-control'}),
        }