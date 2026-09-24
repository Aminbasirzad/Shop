from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
from .forms import SignUpForm


from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms import SignUpForm


def sign_up(request):

    if request.method == 'POST':

        form = SignUpForm(request.POST)

        if form.is_valid():

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            if User.objects.filter(username=email).exists():

                return render(
                    request,
                    'account/sign-up.html',
                    {
                        'form': form,
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

    else:
        form = SignUpForm()

    return render(
        request,
        'account/sign-up.html',
        {
            'form': form
        }
    )

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


def sign_out(request):
    logout(request)
    return redirect('home')