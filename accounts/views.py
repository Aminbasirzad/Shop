from django.shortcuts import render

def sign_in(request):
  return render(request, 'account/sign-in.html')

def sign_up(request):
  return render(request, 'account/sign-up.html')
