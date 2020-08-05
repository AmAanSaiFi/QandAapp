from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from .forms import SignUpForm

# Create your views here.
def signup(req):
    if req.method == 'POST':
        form = SignUpForm(req.POST, req.FILES)
        if form.is_valid():
            user = form.save()
            auth_login(req, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(req, 'signup.html', {'form':form})