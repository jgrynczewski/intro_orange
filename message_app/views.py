from django.shortcuts import render, redirect

from message_app.models import Message


# html form
def contact1(request):
    if request.method == "POST":
        data = request.POST
        email = data.get('email')
        category = data.get('category')
        subject = data.get('subject')
        body = data.get('body')
        fav_date = data.get('fav_date')
        fav_time = data.get('fav_time')

        Message.objects.create(
            email=email,
            category=category,
            subject=subject,
            body=body,
            fav_date=fav_date,
            fav_time=fav_time,
        )
        return redirect('message_app:contact1')

    return render(
        request,
        'message_app/contact1.html',
    )
