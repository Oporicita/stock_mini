from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from products.models import Product
from transactions.models import Transaction
from inventory.models import Inventory

@login_required
def dashboard(request):
    total_products = Product.objects.count()
    total_transactions = Transaction.objects.count()
    low_stock_items = Inventory.objects.filter(quantity__lte=10)
    low_stock = low_stock_items.count()
    total_stock = sum(i.quantity for i in Inventory.objects.all())
    recent_transactions = Transaction.objects.order_by('-date')[:5]
    context = {
        'total_products': total_products,
        'total_transactions': total_transactions,
        'low_stock': low_stock,
        'total_stock': total_stock,
        'low_stock_items': low_stock_items,
        'recent_transactions': recent_transactions,
    }
    return render(request, 'dashboard/dashboard.html', context)
