from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegisterForm
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)

@login_required
def Home(request):
    return render(request, 'LRS/home.html', {})

def login_view(request):
    next = request.GET.get('next')
    form = LoginForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(username=username, password=password)
        login(request, user)

        if next:
            return redirect(next)

        return redirect('home')

    return render(request, 'LRS/login.html', {'form': form})

def Register(request):
    next = request.GET.get('next')
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        n_user = authenticate(username=user.username, password=password)
        login(request, n_user)

        if next:
            return redirect(next)

        return redirect('home')

    return render(request, 'LRS/register.html', {'form': form})


def Logout(request):
    logout(request)
    return redirect('login')