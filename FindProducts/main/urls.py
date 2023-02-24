from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    
    path("", views.home, name="home"),
    path("product", views.product, name="product"),
    path("payment", views.payment, name="payment"),
    path("payment", views.payment, name="payment"),


]