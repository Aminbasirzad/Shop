from django.shortcuts import render

def service(request):
  return render(request, 'services/services.html')

def services_detail(request):
  return render(request, 'services/service-details.html')