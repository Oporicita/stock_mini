from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('products/', include('products.urls')),
    path('suppliers/', include('suppliers.urls')),
    path('inventory/', include('inventory.urls')),
    path('purchase-orders/', include('purchase_orders.urls')),
    path('transactions/', include('transactions.urls')),
    path('reports/', include('reports.urls')),
]
