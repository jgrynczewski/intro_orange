from datetime import datetime

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


def hello2(request):
    return render(
        request,
        'hello.html'
    )


def name2(request, data):
    return render(
        request,
        'name.html',
        context={
            "data": data
        }
    )


# Widok - warstwa logiki
# Szablon - warstwa prezentacji (DTL - Django Template Language)
def is_it_new_year(request):
    now = datetime.now()

    is_new_year = False
    if now.day == 1 and now.month == 1:
        is_new_year = True

    return render(
        request,
        'is_it_new_year.html',
        context={
            'is_new_year': is_new_year,
        }
    )
