from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


def sign_up(request):

    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=email).exists():

            return render(
                request,
                'account/sign-up.html',
                {
                    'error': 'این ایمیل قبلاً ثبت شده است.'
                }
            )

        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=name
        )

        login(request, user)

        return redirect('home')

    return render(request, 'account/sign-up.html')

def sign_in(request):

    if request.method == 'POST':

        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=email,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('home')

        return render(
            request,
            'account/sign-in.html',
            {
                'error': 'ایمیل یا رمز عبور اشتباه است.'
            }
        )

    return render(
        request,
        'account/sign-in.html'
    )