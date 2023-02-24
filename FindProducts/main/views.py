from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse

# Create your views here.
def index(request :HttpRequest):

    return render(request ,'main/index.html')

def home(request :HttpRequest):

    return render(request ,'main/home.html')

def product (request :HttpRequest):

    return render(request ,'main/product.html')


def payment (request :HttpRequest):

    return render(request ,'main/payment.html')

def order (request :HttpRequest):

    return render(request ,'main/order.html')

def order_summary(request :HttpRequest):

    return render(request ,'main/order_summary.html')







