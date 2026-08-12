from django.db import models
from django.utils.text import slugify



class Category(models.Model):
  name = models.CharField(max_length=100)
  slug = models.SlugField(unique=True)
  class Meta:
    ordering = ['name']
    verbose_name_plural = 'Categories'

  def save(self, *args, **kwargs):
    if not self.slug:
      self.slug = slugify(self.name)
    super().save(*args, **kwargs)

  def __str__(self):
    return self.name

class Product(models.Model):
  category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products', verbose_name='دسته')
  name = models.CharField(max_length=255, verbose_name='نام محصول')
  slug = models.SlugField(unique=True)
  description = models.TextField(verbose_name='توضیحات')
  price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='قیمت اصلی')
  discounted_percentage = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name='درصد تخفیف')
  stock = models.PositiveIntegerField(default=0, verbose_name='موجودی')
  is_active = models.BooleanField(default=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  sku = models.CharField(max_length=50, unique=True, verbose_name='کد محصول')
  seller = models.CharField(max_length=100, default='فروشگاه من')

  class Meta:
    ordering = ['-created_at']
    verbose_name = "محصول"
    verbose_name_plural = "محصولات"

  def save(self, *args, **kwargs):
        if not self.slug:
          self.slug = slugify(self.name)
        super().save(*args, **kwargs)

  def __str__(self):
    return self.name

  @property
  def final_price(self):
    """محاسبه قیمت نهایی پس از اعمال تخفیف"""
    if self.discounted_percentage > 0:
      return self.price * (1 - self.discounted_percentage / 100)
    return self.price

class ProductImage(models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='image')
  image = models.ImageField(upload_to='products/', blank=True, null=True)
  is_main = models.BooleanField(default=False, verbose_name='تصویر اصلی')

  def __str__(self):
    return f"Image for {self.product.name}"


class Color(models.Model):
  name = models.CharField(max_length=50)
  code = models.CharField(max_length=20, help_text=000000, verbose_name='کد رنگ')

  def __str__(self):
    return self.name


class ProductVariant(models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variants')
  color = models.ForeignKey(Color, on_delete=models.PROTECT)
  price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
  stock = models.PositiveIntegerField(default=0)
  image = models.ImageField(upload_to='products/variants/', null=True, blank=True)

  def __str__(self):
    return f"{self.product.name} - {self.color.name}"

class Order(models.Model):
  name = models.CharField(max_length=100, verbose_name='نام')
  phone = models.CharField(max_length=20, verbose_name='شماره تماس')
  address = models.TextField(verbose_name='آدرس')
  total_price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='مبلغ کل')
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.name} - {self.id}"

class OrderItem(models.Model):
  order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
  product = models.ForeignKey(Product, on_delete=models.PROTECT)
  quantity = models.PositiveBigIntegerField(default=1)
  price = models.DecimalField(max_digits=12, decimal_places=2)

  def __str__(self):
    return f"{self.product.name} - {self.quantity}"