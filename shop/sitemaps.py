from django.contrib.sitemaps import Sitemap
from .models import Product, Category

class ProductSitemap(Sitemap):
  def items(self):
    return Product.objects.filter(is_active=True)

  def location(self, item):
    return item.get_absolute_url()