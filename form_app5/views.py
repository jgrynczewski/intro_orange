from django.shortcuts import render, redirect

from form_app5.models import Task


def task_create_view(request):
    if request.method == "GET":
        return render(
            request,
            'form_app5/task_form.html',
        )

    if request.method == "POST":
        task = request.POST.get('task')
        if task:
            # zapis do tabeli Task
            Task.objects.create(name=task)

        return redirect("form_app5:task_list_view")


def task_list_view(request):
    # odczyt z tabeli Task
    tasks = Task.objects.all()

    return render(
        request,
        'form_app5/task_list.html',
        context={
            'tasks': tasks,
        }
    )
