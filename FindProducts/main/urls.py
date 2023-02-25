from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    
    path("", views.home, name="home"),
    path("product", views.product, name="product"),
    path("cart", views.cart, name="cart"),
    path("Nahdi", views.Nahdi, name="Nahdi"),
    path("dawaa", views.dawaa, name="dawaa"),
    path("whites", views.whites, name="whites"),
    path("kunooz", views.kunooz, name="kunooz")




]