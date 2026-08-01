from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request, 'home/index.html')

def home_v2(request):
  return render(request, 'home/index-2.html')

def home_v3(request):
  return render(request, 'home/index-3.html')

def base(request):
  return render(request, 'home/base.html')


