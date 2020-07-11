from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from auth.forms import SignUpForm


def home(request):
    return render(
        request,
        'home.html'
    )


def signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data.get('username'))
            print(form.cleaned_data.get('password1'))
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(
        request,
        'signup.html',
        {'form': form},
    )
