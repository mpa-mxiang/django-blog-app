from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def user_login(request):
    return render(request, 'blog/login.html')

def signup(request):
    return render(request, 'blog/signup.html')
    
def home(request):
    return render(request, 'blog/home.html')