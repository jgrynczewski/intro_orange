from django.shortcuts import render, HttpResponse

from django import views
from django.views.generic import TemplateView

# function view
def hello(request):
    return HttpResponse("Hello, world!")


# class view
class HelloView(views.View):
    def get(self, request):
        return HttpResponse("Hello, world!")


# function view (widok funkcyjny)
def hello_function_view(request):
    return render(
        request,
        'view_app/hello.html'
    )


# class view (widok klasowy)
class HelloClassView(views.View):
    def get(self, request):
        return render(
            request,
            'view_app/hello.html'
        )


# generic class view (widok generyczny)
class HelloGenericView(TemplateView):
    template_name = 'view_app/hello.html'
