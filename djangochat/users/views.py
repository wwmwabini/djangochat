from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm

def register(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)

        if register_form.is_valid():
            register_form.save()

            return redirect('user-login')
    else:
        register_form = RegisterForm()

    context = {
        'register_form': register_form
    }
    return render(request, 'users/register.html', context=context)