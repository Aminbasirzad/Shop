from django.urls import path
from . import views

urlpatterns = [
  path('home/', views.home, name='home'),
  path('home_v2/', views.home_v2, name='home_v2'),
  path('home_v3/', views.home_v3, name='home_v3')
]