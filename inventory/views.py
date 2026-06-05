from django.shortcuts import render, get_object_or_404, redirect
from .models import Inventory
from products.models import Product

def inventory_list(request):
    inventory = Inventory.objects.all()
    return render(request, 'inventory/inventory_list.html', {'inventory': inventory})

def inventory_add(request):
    if request.method == 'POST':
        product_id = request.POST['product']
        quantity = request.POST['quantity']
        low_stock_threshold = request.POST['low_stock_threshold']
        product = Product.objects.get(pk=product_id)
        Inventory.objects.create(product=product, quantity=quantity, low_stock_threshold=low_stock_threshold)
        return redirect('inventory_list')
    products = Product.objects.all()
    return render(request, 'inventory/inventory_form.html', {'products': products})

def inventory_edit(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    if request.method == 'POST':
        inventory.quantity = request.POST['quantity']
        inventory.low_stock_threshold = request.POST['low_stock_threshold']
        inventory.save()
        return redirect('inventory_list')
    return render(request, 'inventory/inventory_form.html', {'inventory': inventory})

def inventory_delete(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    inventory.delete()
    return redirect('inventory_list')
