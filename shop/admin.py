from django.contrib import admin
from .models import Product, Category, ProductImage, Color, ProductVariant, Order, OrderItem

admin.site.register(Product)

admin.site.register(Category)

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
  list_display = ['product', 'image', 'is_main']

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
  list_display = ['name', 'code']

@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
  list_display = ['product', 'color', 'stock']

admin.site.register(OrderItem)

admin.site.register(Order)
