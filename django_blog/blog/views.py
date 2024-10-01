from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts

# Create your views here.

def user_login(request):
    return render(request, 'blog/login.html')

def signup(request):
    return render(request, 'blog/signup.html')
    
def home(request):
    context = {
        'posts': Posts.objects.all()
    }
    return render(request, 'blog/home.html', context)