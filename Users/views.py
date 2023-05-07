from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from . import forms
from django.contrib.auth import authenticate, login, logout


# Create your views here.


def registration_view(request):
    form = forms.RegistrationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        else:
            return render(request, 'Users/registration_form.html', {'form': form})

        return redirect(reverse_lazy('Users:login'))

    return render(request, 'Users/registration_form.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = forms.LoginForm(request, request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(email=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(reverse_lazy('Home:home'))

    else:
        form = forms.LoginForm()
    return render(request, 'Users/login_form.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect(reverse_lazy('Home:home'))
