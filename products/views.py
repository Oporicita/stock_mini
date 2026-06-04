from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def product_add(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        quantity = request.POST['quantity']
        Product.objects.create(name=name, description=description, price=price, quantity=quantity)
        return redirect('product_list')
    return render(request, 'products/product_form.html')

def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.name = request.POST['name']
        product.description = request.POST['description']
        product.price = request.POST['price']
        product.quantity = request.POST['quantity']
        product.save()
        return redirect('product_list')
    return render(request, 'products/product_form.html', {'product': product})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('product_list')
@csrf_exempt
def api_product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        data = list(products.values('id', 'name', 'description', 'price', 'quantity'))
        return JsonResponse(data, safe=False)

    if request.method == 'POST':
        body = json.loads(request.body)
        product = Product.objects.create(
            name=body['name'],
            description=body['description'],
            price=body['price'],
            quantity=body['quantity']
        )
        return JsonResponse({'id': product.id, 'message': 'Created'})
