from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("login/", views.user_login),
    path("signup/", views.signup),
    path("mypost/", views.my_post),
    path("newpost/", views.new_post)
    path("signout/",  views.signout)
]
