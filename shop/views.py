from django.shortcuts import render, get_object_or_404
from .models import Product

def product_detail(request, id):
  product = get_object_or_404(Product, id=id)
  return render(request, 'products/product-details.html', {'product':product})

def products(request):
  products = Product.objects.all()
  return render(request, 'products/products.html', {"products":products})

def cart(request):
  return render(request, 'products/cart.html')

def checkout(request):
  return render(request, 'products/checkout.html')