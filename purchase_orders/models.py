from django.db import models
from suppliers.models import Supplier
from products.models import Product

class PurchaseOrder(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('received', 'Received'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"PO-{self.id} - {self.product.name}"
