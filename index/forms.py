from django import forms
from django.forms import ModelForm, TextInput, SelectMultiple, Select

from .models import Producto, Rate

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['name', 'marca', 'sku', 'categoria']
        widgets = {
            'name': TextInput(attrs={'class':'form-control', 'placeholder':'Nombre Producto'}),
            'marca': TextInput(attrs={'class':'form-control', 'placeholder':'Marca'}),
            'sku': TextInput(attrs={'class':'form-control', 'placeholder':'Codigo'}),
            'categoria': SelectMultiple(attrs={'class':'form-control' })
        }
        labels = {
            'name': 'Nombre'
        }

class RateForm(ModelForm):
    class Meta:
        model = Rate
        fields = ['product', 'rate']
        widgets = {
            'product': Select(attrs={'class':'form-control product-rate-select'})
        }
        labels = {
            'product' : 'Producto'
        }
