from django.contrib.auth.handlers.modwsgi import check_password
from django.contrib.auth.hashers import make_password
from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.pk} {self.username} {self.role}'

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)


class Condractor_on_stock(models.Model):
    company = models.CharField(max_length=100)
    number = models.PositiveIntegerField()
    email = models.CharField(max_length=100)
    condition = models.CharField(max_length=100, null=True, blank=True)
    quantity = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.pk} {self.company} {self.number} {self.condition} {self.quantity}'


class Product(models.Model):
    condractor_on_stock = models.ForeignKey(Condractor_on_stock, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    text = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.pk} {self.name} {self.category} {self.text} {self.quantity}'


class Staff(models.Model):
    efficiency = models.BooleanField()
    control = models.BooleanField()
    condition = models.CharField(max_length=100, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f'{self.pk} {self.efficiency} {self.control} {self.condition}'


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveIntegerField()
    condition = models.CharField(max_length=100)
    shipping = models.BooleanField()

    def __str__(self):
        return f'{self.pk} {self.condition} {self.quantity} {self.shipping}'


class Condractor_for_the_stock(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    number = models.PositiveIntegerField()
    email = models.CharField(max_length=100)
    condition = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.pk} {self.number} {self.email} {self.condition} {self.quantity}'



