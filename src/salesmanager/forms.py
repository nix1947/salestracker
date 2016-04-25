from django.forms import ModelForm
from django import forms
from .models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        exclude = ('created_at', 'updated_at',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Item Name"}),
            'tag':forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Item Tag"}),
            'category':forms.Select(attrs={'class': 'form-control', 'placeholder':"Item Category"}),
            'company':forms.Select(attrs={'class': 'form-control'}),
            'price':forms.NumberInput(attrs={'class': 'form-control'}),
            'status':forms.Select(attrs={'class': 'form-control'}),
        }
