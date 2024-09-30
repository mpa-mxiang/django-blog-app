from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("login/", views.user_login),
    path("signup/", views.signup),
]
