from django.urls import path
from . import views


urlpatterns = [
  path('product_detail/<int:id>/', views.product_detail, name='product_detail'),
  path('products/', views.products, name='products'),
  path('cart/', views.cart, name='cart'),
  path('checkout/', views.checkout, name='checkout'),
  path('add-to-cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
  path('cart/remove/<int:id>/', views.remove_from_cart, name='remove_from_cart'),
  path('cart/update/<int:id>/', views.update_cart, name='update_cart'),
  path('order-success/', views.order_success, name='order_success'),
  path('my_orders/', views.my_orders, name='my_orders'),
  path('order-detail/<int:id>/', views.order_detail, name='order_detail'),
  path('product/<int:id>/review/', views.add_review, name='add_review'),
  path('review/<int:id>/delete/', views.delete_review, name='delete_review'),
  path('review/<int:id>/edit/', views.edit_review, name='edit_review'),

]
