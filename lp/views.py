from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import logout
# Create your views here.
# lp/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import LoginForm, RegistrationForm
from django.contrib.auth.models import User

# Home view
def home(request):
    return render(request, 'accounts/home.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, "Invalid login credentials")
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})


# Register view
def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)  # Log the user in immediately after registration
            return redirect('home')
    else:
        form = RegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to home or wherever you want after logout
