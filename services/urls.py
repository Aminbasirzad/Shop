from django.urls import path
from . import views

urlpatterns = [
  path('service/', views.service, name='service'),
  path('services_detail/', views.services_detail, name='services_detail'),
]