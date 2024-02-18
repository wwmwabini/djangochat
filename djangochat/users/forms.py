from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError

def validate_email(form_email):
    if User.objects.filter(email=form_email).exists():
        raise ValidationError(f'{form_email} already exists in our system', params={'form_email': form_email})

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(min_length=2, max_length=32)
    last_name = forms.CharField(min_length=2, max_length=32)
    email = forms.EmailField(validators=[validate_email])

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']