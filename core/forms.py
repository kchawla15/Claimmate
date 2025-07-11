from django import forms
from .models import WarrantyItem, Expense  # Make sure Expense is imported

class WarrantyItemForm(forms.ModelForm):
    class Meta:
        model = WarrantyItem
        fields = [
            'store_name',
            'product_type',
            'warranty_duration_days',
            'purchase_date',
            'receipt_file',
            'price',  # Added price field
        ]
        widgets = {
            'purchase_date': forms.DateInput(attrs={'type': 'date'}),
            'price': forms.NumberInput(attrs={'step': '0.01', 'min': '0'}),
        }

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['date', 'category', 'description', 'price']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'price': forms.NumberInput(attrs={'step': '0.01', 'min': '0'}),
        }
