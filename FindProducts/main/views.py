from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse

# Create your views here.
def index(request :HttpRequest):

    return render(request ,'main/index.html')

def home(request :HttpRequest):

    return render(request ,'main/home.html')

def product (request :HttpRequest):

    return render(request ,'main/product.html')


def cart (request :HttpRequest):

    return render(request ,'main/cart.html')

def Nahdi (request :HttpRequest):

    return render(request ,'main/Nahdi.html')

def dawaa(request :HttpRequest):

    return render(request ,'main/dawaa.html')

def whites(request :HttpRequest):

    return render(request ,'main/whites.html')

def kunooz(request :HttpRequest):

    return render(request ,'main/kunooz.html')








