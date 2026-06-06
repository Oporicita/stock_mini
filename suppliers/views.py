from django.shortcuts import render, redirect, get_object_or_404
from .models import Supplier

def supplier_list(request):
    suppliers = Supplier.objects.all()
    return render(request, 'suppliers/supplier_list.html', {'suppliers': suppliers})


def supplier_add(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        Supplier.objects.create(name=name, phone=phone)
        return redirect('supplier_list')
    return render(request, 'suppliers/supplier_form.html')


def supplier_edit(request, id):
    supplier = get_object_or_404(Supplier, id=id)
    if request.method == 'POST':
        supplier.name = request.POST['name']
        supplier.phone = request.POST['phone']
        supplier.save()
        return redirect('supplier_list')
    return render(request, 'suppliers/supplier_form.html', {'supplier': supplier})


def supplier_delete(request, id):
    supplier = get_object_or_404(Supplier, id=id)
    supplier.delete()
    return redirect('supplier_list')
