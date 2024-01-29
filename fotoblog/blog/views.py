from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'blog/home.html')

@login_required
def password_change_done(request):
    return render(request, 'blog/password_change_done.html')

