from django.shortcuts import render, HttpResponse
from django.utils.html import escape


# Create your views here.
def hello(request):
    return HttpResponse("Hello, world!")


def eva(request):
    return HttpResponse("Hello, Eva!")


def adam(request):
    return HttpResponse("Hello, Adam!")


def name(request, data):
    # Podatność xss
    # XSS - Cross Site Scripting

    # Always remember to escape your output
    print(data)
    escaped_data = escape(data)
    print(escaped_data)
    return HttpResponse(f"Hello, {escaped_data}!")

