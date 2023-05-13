from django.shortcuts import render, HttpResponse


# function view
def hello(request):
    return HttpResponse("Hello, world!")

