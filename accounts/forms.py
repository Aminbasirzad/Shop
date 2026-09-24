from django import forms
from captcha.fields import CaptchaField

class SignUpForm(forms.Form):
  name = forms.CharField(max_length=100)
  email = forms.EmailField()
  password = forms.CharField(widget=forms.PasswordInput)
  captcha = CaptchaField()