from django.urls import path
from . import views

urlpatterns = [
  path('case_study/', views.case_study, name='case_study'),
  path('case_study_detail/', views.case_study_detail, name='case_study_detail'),
]