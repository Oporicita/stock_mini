from django.shortcuts import render, get_object_or_404, redirect
from .models import Supplier

def supplier_list(request):
    suppliers = Supplier.objects.all()
    return render(request, 'suppliers/supplier_list.html', {'suppliers': suppliers})

def supplier_add(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        Supplier.objects.create(name=name, email=email, phone=phone, address=address)
        return redirect('supplier_list')
    return render(request, 'suppliers/supplier_form.html')

def supplier_edit(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method == 'POST':
        supplier.name = request.POST['name']
        supplier.email = request.POST['email']
        supplier.phone = request.POST['phone']
        supplier.address = request.POST['address']
        supplier.save()
        return redirect('supplier_list')
    return render(request, 'suppliers/supplier_form.html', {'supplier': supplier})

def supplier_delete(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    supplier.delete()
    return redirect('supplier_list')
