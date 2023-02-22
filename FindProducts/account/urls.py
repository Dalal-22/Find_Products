from django.urls import path
from . import views

app_name = "account"
urlpatterns = [
    path("", views.checkout, name="checkout"),
    path("login", views.login, name="login"),
    path("register", views.register, name="register")
    
]

