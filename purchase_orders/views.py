from django.shortcuts import render, get_object_or_404, redirect
from .models import PurchaseOrder
from products.models import Product
from suppliers.models import Supplier

def purchase_order_list(request):
    orders = PurchaseOrder.objects.all()
    return render(request, 'purchase_orders/purchase_order_list.html', {'orders': orders})

def purchase_order_add(request):
    if request.method == 'POST':
        product_id = request.POST['product']
        supplier_id = request.POST['supplier']
        quantity = request.POST['quantity']
        status = request.POST['status']
        product = Product.objects.get(pk=product_id)
        supplier = Supplier.objects.get(pk=supplier_id)
        PurchaseOrder.objects.create(product=product, supplier=supplier, quantity=quantity, status=status)
        return redirect('purchase_order_list')
    products = Product.objects.all()
    suppliers = Supplier.objects.all()
    return render(request, 'purchase_orders/purchase_order_form.html', {'products': products, 'suppliers': suppliers})

def purchase_order_edit(request, pk):
    order = get_object_or_404(PurchaseOrder, pk=pk)
    if request.method == 'POST':
        order.quantity = request.POST['quantity']
        order.status = request.POST['status']
        order.save()
        return redirect('purchase_order_list')
    return render(request, 'purchase_orders/purchase_order_form.html', {'order': order})

def purchase_order_delete(request, pk):
    order = get_object_or_404(PurchaseOrder, pk=pk)
    order.delete()
    return redirect('purchase_order_list')
