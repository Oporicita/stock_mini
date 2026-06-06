from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
    path('', include('dashboard.urls')),
    path('products/', include('products.urls')),
    path('suppliers/', include('suppliers.urls')),
    path('inventory/', include('inventory.urls')),
    path('purchase-orders/', include('purchase_orders.urls')),
    path('transactions/', include('transactions.urls')),
    path('reports/', include('reports.urls')),
]
