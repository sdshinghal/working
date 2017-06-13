from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    return HttpResponse("This is the home page")

#making some changes here

def next_page(request):
    return HttpResponse("This will be the next page")