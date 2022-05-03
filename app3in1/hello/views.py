from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'hello/index.html')

def willian(request):
    return HttpResponse("Hello, Willian. You're at the hello index.")

def benicio(request):
    return HttpResponse("Hello, Benicio. You're at the hello index.")
    
def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })
