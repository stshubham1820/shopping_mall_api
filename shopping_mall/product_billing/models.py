from django.db import models
from shopping_mall.product.models import Product
from shopping_mall.users.models import User
from shopping_mall.customer.models import Customer


class ProductBilling(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    final_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def calculate_final_price(self):
        price_per_unit = self.product.price
        discounted_price = float(price_per_unit) * (1 - float(self.discount) / 100)
        self.final_price = discounted_price * self.quantity
        return self.final_price

    def save(self, *args, **kwargs):
        self.calculate_final_price()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product.name} - {self.quantity} units"

class Invoice(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    sold_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='invoices_sold')
    products = models.ManyToManyField(ProductBilling, related_name='invoices')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.customer.name} - {self.total_amount}"
        