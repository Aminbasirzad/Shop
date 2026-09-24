from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage
from shop.models import Review
from accounts.forms import ContactForm

def page_not_found(request):
  return render(request, 'pages/404.html')

def about(request):
  reviews = Review.objects.select_related('user', 'product').order_by('-created_at')[:5]
  return render(request, 'pages/about-us.html', {'reviews':reviews})

def faq(request):
  return render(request, 'pages/faq.html')

def privacy_policy(request):
  return render(request, 'pages/privacy-policy.html')

def terms_conditions(request):
  return render(request, 'pages/terms-conditions.html')

def contact(request):

    if request.method == 'POST':

        form = ContactForm(request.POST)

        if form.is_valid():

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )

            messages.success(
                request,
                "پیام شما با موفقیت ارسال شد"
            )

            return redirect('contact')

    else:
        form = ContactForm()

    return render(
        request,
        'pages/contact-us.html',
        {
            'form': form
        }
    )
