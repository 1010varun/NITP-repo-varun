import http
from django.shortcuts import render , HttpResponse

# Create your views here.
def index(request):
    return render(request , 'index.html')

def login(request):
    return render(request , 'login.html')

def purchase(request):
    return render(request , 'purchase.html')

def register(request):
    return render(request , 'register.html')