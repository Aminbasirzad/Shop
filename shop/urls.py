from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('product_detail/<int:id>/', views.product_detail, name='product_detail'),
  path('products/', views.products, name='products'),
  path('cart/', views.cart, name='cart'),
  path('checkout/', views.checkout, name='checkout'),
]
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, docunent_root=settings.MEDIA_ROOT)