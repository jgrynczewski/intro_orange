from django.shortcuts import render, HttpResponse


# Create your views here.
def hello(request):
    return HttpResponse("Hello, world!")


def eva(request):
    return HttpResponse("Hello, Eva!")


def adam(request):
    return HttpResponse("Hello, Adam!")


def name(request, data):
    return HttpResponse(f"Hello, {data}!")
