from django.shortcuts import render
from transactions.models import Transaction
from products.models import Product
from inventory.models import Inventory

def report_view(request):
    transactions = Transaction.objects.all()
    low_stock = Inventory.objects.filter(quantity__lte=10)
    total_stock_in = sum(t.quantity for t in transactions.filter(transaction_type='in'))
    total_stock_out = sum(t.quantity for t in transactions.filter(transaction_type='out'))
    context = {
        'transactions': transactions,
        'low_stock': low_stock,
        'total_stock_in': total_stock_in,
        'total_stock_out': total_stock_out,
    }
    return render(request, 'reports/report.html', context)
