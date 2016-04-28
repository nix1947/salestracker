from django.forms import ModelForm
from django import forms
from .models import Item, Company

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
            'selling_price':forms.NumberInput(attrs={'class': 'form-control'}),
            'status':forms.Select(attrs={'class': 'form-control'}),
        }


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        exclude = ('created_at', 'updated_at')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Company Name"}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Company Phone"}),
            'mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Company mobile"}),
            'address': forms.Select(attrs={'class': 'form-control', 'placeholder': "Company Phone"}),
            'contact_person': forms.Select(attrs={'class': 'form-control', 'placeholder': "Company Phone"}),
        }
