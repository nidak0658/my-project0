from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone

class MenuItem(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name

class Table(models.Model):
    number = models.IntegerField(unique=True)
    capacity = models.IntegerField()

    def __str__(self):
        return f"Table {self.number}"

class Reservation(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    guest_name = models.CharField(max_length=100)
    guest_phone = models.CharField(max_length=20)
    reservation_time = models.DateTimeField()

    def __str__(self):
        return f"{self.guest_name} - {self.reservation_time}"

class Order(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    items = models.ManyToManyField(MenuItem, through='OrderItem')
    created_at = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Order for Table {self.table.number}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.item.name}"

class Inventory(models.Model):
    item = models.OneToOneField(MenuItem, on_delete=models.CASCADE)
    stock = models.IntegerField()

    def __str__(self):
        return f"{self.item.name} - Stock: {self.stock}"
