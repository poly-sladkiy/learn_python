from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from accounts.forms import UserLoginForm, UserRegistrationForm


def login_view(request):
    form = UserLoginForm(request.POST or None)
    _next = request.POST.get('next')

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(username=username, password=password)

        login(request, user)

        _next = _next or '/'
        return redirect(_next)

    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')


def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            new_user = form.save(commit=False)  # Будет создан экземпляр, но пока не сохранен
            new_user.set_password(form.cleaned_data['password2'])  # Устанавливаем пароль
            new_user.save()  # Сохраняем

            return render(request, 'accounts/register_done.html', {'new_user': new_user})

        return render(request, 'accounts/register.html', {'form': form})

    else:
        form = UserRegistrationForm()
        return render(request, 'accounts/register.html', {'form': form})
