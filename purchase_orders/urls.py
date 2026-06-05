from django.urls import path
from . import views

urlpatterns = [
    path('', views.purchase_order_list, name='purchase_order_list'),
    path('add/', views.purchase_order_add, name='purchase_order_add'),
    path('edit/<int:pk>/', views.purchase_order_edit, name='purchase_order_edit'),
    path('delete/<int:pk>/', views.purchase_order_delete, name='purchase_order_delete'),
]
