from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

@login_required
def profile(request):
    return render(request, 'users/profile.html')

def register(request):
    if request.method == 'POST':
        r_form = UserRegisterForm(request.POST)
        if r_form.is_valid():
            r_form.save()
            username = r_form.cleaned_data.get('username')
            messages.success(request, f'{username}, Twoje konto zostało utworzone!')
            return redirect('home')
    else:
        r_form = UserRegisterForm()
    return render(request, 'users/register.html', {'r_form': r_form})

