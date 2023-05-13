from django.shortcuts import render


# Create na ciasteczkach
def set_cookie(request):
    response = render(
        request,
        'state_app/cookies.html',
    )
    response.set_cookie('ciasteczko1', 5)
    response.set_cookie('ciasteczko2', 10, max_age=45)  # max_age podawane w sekundach

    return response


# Read na ciasteczkach
def show_cookies(request):
    cookies = request.COOKIES

    return render(
        request,
        'state_app/show.html',
        context={
            'cookies': cookies,
        }
    )


# Delete na ciasteczkach
def delete_cookie(request):
    response = render(
        request,
        'state_app/cookies.html',
    )
    response.delete_cookie('ciasteczko1')

    return response
