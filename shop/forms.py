from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
  class Mete:
    model = Order
    fields = ['name', 'phone', 'address']