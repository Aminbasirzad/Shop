from django.urls import path
from . import views

urlpatterns = [
  path('product_detail/', views.product_detail, name='product_detail'),
  path('products/', views.products, name='products'),
  path('cart/', views.cart, name='cart'),
  path('checkout/', views.checkout, name='checkout'),
]