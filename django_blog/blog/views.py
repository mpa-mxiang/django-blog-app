from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Posts
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def user_login(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        password = request.POST.get('upassword')
        login_user = authenticate(request, username = name, password = password)
        if login_user is not None:
            login(request, login_user)
            return redirect('/')
        else:
            return redirect('/login')
    return render(request, 'blog/login.html')

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        email = request.POST.get('uemail')
        password = request.POST.get('upassword')
        new_user = User.objects.create_user(username = name, email = email, password = password)
        new_user.save()
        return redirect('/login')
    return render(request, 'blog/signup.html')
    
def home(request):
    context = {
        'posts': Posts.objects.all()
    }
    return render(request, 'blog/home.html', context)