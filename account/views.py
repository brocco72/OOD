from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'حساب کاربری با موفقیت ایجاد شد')
            return redirect('register-success')
    else:
        form = UserRegistrationForm()
    return render(request, 'account/register.html', {'form': form})


def register_success(request):
    return render(request, 'account/register-success.html')
