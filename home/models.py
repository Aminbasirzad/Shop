from django.db import models

# Create your models here.

class Category(models.Model):
  name = models.CharField(max_length=100)
  slug = models.SlugField(unique=True)
  def __str__(self):
    return self.name

class Product(models.Model):
  category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
  name = models.CharField(max_length=255, verbose_name='نام محصول')
  slug = models.SlugField(unique=True)
  description = models.TextField(blank=True)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  stock = models.PositiveIntegerField(default=0)
  image = models.ImageField(upload_to='products/%Y/%m/%d')
  is_active = models.BooleanField(default=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  sku = models.CharField(max_length=50, unique=True)

  def __str__(self):
    return self.name