from django.shortcuts import render
from products.models import Product
from transactions.models import Transaction
from inventory.models import Inventory

def dashboard(request):
    total_products = Product.objects.count()
    total_transactions = Transaction.objects.count()
    low_stock_items = Inventory.objects.filter(quantity__lte=10)
    low_stock = low_stock_items.count()
    total_stock = sum(i.quantity for i in Inventory.objects.all())
    context = {
        'total_products': total_products,
        'total_transactions': total_transactions,
        'low_stock': low_stock,
        'total_stock': total_stock,
        'low_stock_items': low_stock_items,
    }
    return render(request, 'dashboard/dashboard.html', context)
