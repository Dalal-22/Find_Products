from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse

# Create your views here.
def checkout(request :HttpRequest):
    
    return render(request , 'account/checkout.html')

def login(request :HttpRequest):
    
    return render(request , 'account/login.html')
    
def register(request :HttpRequest):
    
    return render(request , 'account/register.html')