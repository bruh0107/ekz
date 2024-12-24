from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .forms import UserForm
from .models import User


def home(request):
    return render(request, 'store/index.html')

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Аккаунт создан')
            return redirect('ekz:login')
    else:
        form = UserForm()
    return render(request, 'store/register.html', {'form': form})

@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, "store/profile.html", {'user_profile': user})