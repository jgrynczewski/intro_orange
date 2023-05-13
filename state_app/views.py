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
        'state_app/show_cookies.html',
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


# Create na sesji
def set_session(request):
    request.session['num_visit'] = 0

    return render(
        request,
        'state_app/session.html',
    )


# Read na sesji
def show_session(request):
    num_visit = request.session.get('num_visit')

    return render(
        request,
        'state_app/show_session.html',
        context={
            'num_visit': num_visit,
        }
    )


# Update na sesji
def update_session(request):
    num_visit = request.session.get('num_visit', 0)
    request.session['num_visit'] = num_visit + 1

    return render(
        request,
        'state_app/show_session.html',
        context = {
            'num_visit': request.session['num_visit']
        }
    )


# Delete na sesji
def delete_session(request):
    del request.session['num_visit']

    return render(
        request,
        'state_app/session.html',
    )
