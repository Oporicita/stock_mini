from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Supplier

@csrf_exempt
def api_supplier_list(request):
    if request.method == 'GET':
        suppliers = Supplier.objects.all()
        data = list(suppliers.values('id', 'name', 'email', 'phone', 'address'))
        return JsonResponse(data, safe=False)

    if request.method == 'POST':
        body = json.loads(request.body)
        supplier = Supplier.objects.create(
            name=body['name'],
            email=body.get('email', ''),
            phone=body.get('phone', ''),
            address=body.get('address', '')
        )
        return JsonResponse({'id': supplier.id, 'message': 'Created'})
