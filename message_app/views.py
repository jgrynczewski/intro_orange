from django.shortcuts import render, redirect

from message_app.models import Message
from message_app.forms import MessageForm, MessageModelForm


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

        # walidacja na backendzie (my tutaj przepuszczamy wszystko)

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


# django form
def contact2(request):
    if request.method == "POST":
        form = MessageForm(request.POST)  # bound form

        if form.is_valid():
            data = form.cleaned_data
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

            return redirect('message_app:contact2')
        else:
            return render(
                request,
                'message_app/contact2.html',
                context={
                    'form': form,
                }
            )

    elif request.method == "GET":
        form = MessageForm()  # unbound django form

        return render(
            request,
            'message_app/contact2.html',
            context={
                'form': form,
            }
        )


# model form
def contact3(request):
    if request.method == "POST":
        form = MessageModelForm(request.POST)  # bound model form

        if form.is_valid():
            form.save()

            return redirect('message_app:contact2')
        else:
            return render(
                request,
                'message_app/contact3.html',
                context={
                    'form': form,
                }
            )

    if request.method == "GET":
        form = MessageModelForm()  # unbound model form
        return render(
            request,
            'message_app/contact3.html',
            context = {
                'form': form,
            }
        )


# dalsza automatyzacja generowania formularzy jest możliwa z wykorzystaniem biblioteki django-crispy-forms
# https://django-crispy-forms.readthedocs.io/en/latest/
