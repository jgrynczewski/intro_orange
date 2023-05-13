from django.shortcuts import render, HttpResponse

from django import views

# function view
def hello(request):
    return HttpResponse("Hello, world!")


# class view
class HelloView(views.View):
    def get(self, request):
        return HttpResponse("Hello, world!")


# function view
def hello_function_view(request):
    return render(
        request,
        'view_app/hello.html'
    )


# class view
class HelloClassView(views.View):
    def get(self, request):
        return render(
            request,
            'view_app/hello.html'
        )
