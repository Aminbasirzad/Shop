from django.urls import path
from . import views

urlpatterns = [
  path('page_not_found/', views.page_not_found, name='page_not_found'),
  path('about/', views.about, name='about'),
  path('team/',views.team, name='team'),
  path('faq/', views.faq, name='faq'),
  path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
  path('terms_conditions/', views.terms_conditions, name='terms_conditions'),
  path('contact/', views.contact, name='contact'),
  path('testimonials/',views.testimonials, name='testimonials')
]