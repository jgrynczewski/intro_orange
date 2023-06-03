from django.shortcuts import render, redirect

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login, logout


User = get_user_model()


@login_required(login_url='accounts:login_view')
def home(request):
    return render(
        request,
        'accounts/home.html',
    )


def register_view(request):
    if request.method == "GET":
        return render(
            request,
            'accounts/register.html',
        )
    else:
        data = request.POST
        username = data.get('username')
        password1 = data.get('password1')
        password2 = data.get('password2')

        if password1 == password2:
            User.objects.create_user(
                username=username,
                password=password1
            )

        return redirect('accounts:login_view')


def login_view(request):
    if request.method == "GET":
        return render(
            request,
            'accounts/login.html'
        )
    elif request.method == "POST":
        data = request.POST
        username = data.get('username')
        password = data.get('password')

        user = authenticate(
            username=username,
            password=password
        )
        if user:
            login(request, user=user)

        return redirect('accounts:home')


def logout_view(request):
    logout(request)

    return redirect('accounts:home')


def fun_view(request):
    return render(
        request,
        'accounts/fun.html'
    )


@permission_required('accounts.view_user', raise_exception=True)
def secret_view(request):
    return render(
        request,
        'accounts/secret.html'
    )
