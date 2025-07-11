from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout

from .models import WarrantyItem, Expense
from .forms import WarrantyItemForm, ExpenseForm

def home(request):
    return render(request, 'home.html')

@login_required(login_url='login')
def dashboard(request):
    items = WarrantyItem.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'items': items})

@login_required(login_url='login')
def budget_dashboard(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    show_total = False
    total = 0
    if start_date and end_date:
        # Only show total if both dates are set and user clicked Calculate
        from datetime import datetime
        try:
            start = datetime.strptime(start_date, "%Y-%m-%d").date()
            end = datetime.strptime(end_date, "%Y-%m-%d").date()
            items = WarrantyItem.objects.filter(
                user=request.user,
                purchase_date__range=[start, end]
            )
            total = sum(item.price for item in items)
            show_total = True
        except Exception:
            total = 0
            show_total = True
    return render(request, 'budget_dashboard.html', {
        'start_date': start_date,
        'end_date': end_date,
        'total': total,
        'show_total': show_total,
    })

@login_required(login_url='login')
def upload_warranty(request):
    if request.method == 'POST':
        form = WarrantyItemForm(request.POST, request.FILES)
        if form.is_valid():
            warranty = form.save(commit=False)
            warranty.user = request.user
            warranty.save()
            messages.success(request, "Warranty item uploaded successfully.")
            return redirect('dashboard')
    else:
        form = WarrantyItemForm()
    return render(request, 'upload_warranty_item.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login')
        else:
            print("Form errors:", form.errors)  # Debug
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def force_logout(request):
    logout(request)
    return redirect('/')
