from django.db import models
from product.models import Product
from customer.models import Customer
from django.conf import settings

# class Order(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.user} - {self.product.name}"


class Order(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    # transaction_id = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
