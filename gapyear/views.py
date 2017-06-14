from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):

    return render(request, "gapyear/home_page.html")

#making some changes here

def next_page(request):
    return HttpResponse("This will be the next page")

