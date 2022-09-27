from django import forms
from .models import ProductModel
class ProductForm(forms.Form):
    
    class Meta:
        model = ProductModel
        exclude = ['created_at']
        