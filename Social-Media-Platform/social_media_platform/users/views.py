from django.shortcuts import render

# Create your views here.

# users/views.py

from django.shortcuts import render
from .models import User

def profile(request, username):
    user = User.objects.get(username=username)
    return render(request, 'users/profile.html', {'user': user})
