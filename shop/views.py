from django.shortcuts import render

def product_detail(request):
  return render(request, 'products/product-details.html')

def products(request):
  return render(request, 'products/products.html')

def cart(request):
  return render(request, 'products/cart.html')

def checkout(request):
  return render(request, 'products/checkout.html')