from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("index")

def about(request):
    return HttpResponse("about")

def contact(request):
    return HttpResponse("contact")

def portfolio(request):
    return HttpResponse("portfolio")

