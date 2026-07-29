from django.shortcuts import render

def page_not_found(request):
  return render(request, 'pages/404.html')

def about(request):
  return render(request, 'pages/about-us.html')

def team(request):
  return render(request,'pages/team.html')

def faq(request):
  return render(request, 'pages/faq.html')

def privacy_policy(request):
  return render(request, 'pages/privacy-policy.html')

def terms_conditions(request):
  return render(request, 'pages/terms-conditions.html')

def contact(request):
  return render(request, 'pages/contact-us.html')

def testimonials(request):
  return render(request, 'pages/testimonials.html')