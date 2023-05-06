from django.shortcuts import render


# Create your views here.
def first_view(request):
    return render(
        request,
        'links/first_template.html',
    )


def second_view(request):
    return render(
        request,
        'links/second_template.html',
    )


def third_view(request, param):
    return render(
        request,
        'links/third_template.html',
        context={
            'param': param,
        }
    )