from django.shortcuts import render, get_object_or_404, redirect
from .models import Transaction
from products.models import Product

def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request, 'transactions/transaction_list.html', {'transactions': transactions})

def transaction_add(request):
    if request.method == 'POST':
        product_id = request.POST['product']
        transaction_type = request.POST['transaction_type']
        quantity = request.POST['quantity']
        amount = request.POST.get('amount', 0)
        note = request.POST['note']
        product = Product.objects.get(pk=product_id)
        Transaction.objects.create(product=product, transaction_type=transaction_type, quantity=quantity, amount=amount, note=note)
        return redirect('transaction_list')
    products = Product.objects.all()
    return render(request, 'transactions/transaction_form.html', {'products': products})

def transaction_delete(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    transaction.delete()
    return redirect('transaction_list')
