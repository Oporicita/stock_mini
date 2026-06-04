from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.api_supplier_list, name='api_supplier_list'),
]

