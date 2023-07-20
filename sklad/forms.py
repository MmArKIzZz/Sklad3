from django.forms import ModelForm
from .models import *


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ('quantity', 'product')


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'category', 'text', 'quantity', 'condractor_on_stock')


class UseForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'role')


class Condractor_on_stock_Form(ModelForm):
    class Meta:
        model = Condractor_on_stock
        fields = ('company', 'number', 'email')


class StaffForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', )