from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile_no = models.CharField(max_length=15, unique=True)
    address = models.TextField()

    def __str__(self):
        return self.name
