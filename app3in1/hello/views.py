from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the hello index.")

def willian(request):
    return HttpResponse("Hello, Willian. You're at the hello index.")

def benicio(request):
    return HttpResponse("Hello, Benicio. You're at the hello index.")
    
def greet(request, name):
    return HttpResponse(f"Hello, {name}. You're at the hello index.")