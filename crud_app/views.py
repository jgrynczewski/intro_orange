from django.shortcuts import render, redirect, get_object_or_404

from crud_app.models import Task


def task_create_view(request):
    if request.method == "GET":
        return render(
            request,
            'crud_app/task_form.html',
        )

    if request.method == "POST":
        task = request.POST.get('task')
        if task:
            # zapis do tabeli Task
            Task.objects.create(name=task)

        return redirect("crud_app:task_list_view")


def task_list_view(request):
    # odczyt z tabeli Task
    tasks = Task.objects.all()

    return render(
        request,
        'crud_app/task_list.html',
        context={
            'tasks': tasks,
        }
    )


def task_detail_view(request, pk):
    # task = Task.objects.get(id=pk)
    task = get_object_or_404(Task, id=pk)

    return render(
        request,
        'crud_app/task_detail.html',
        context={
            'task': task,
        }
    )


def task_update_view(request, pk):
    task = get_object_or_404(Task, id=pk)

    if request.method == "GET":
        return render(
            request,
            'crud_app/task_update.html',
            context={
                'task': task,
            }
        )

    if request.method == "POST":
        task_new_name = request.POST.get('task')
        if task_new_name:
            task.name = task_new_name
            task.save()

        return redirect("crud_app:task_list_view")


def task_delete_view(request, pk):
    task = get_object_or_404(Task, id=pk)

    if request.method == "GET":
        return render(
            request,
            'crud_app/task_confirm_delete.html',
            context={
                'task': task,
            }
        )

    if request.method == "POST":
        res = request.POST.get('accept')
        if res:
            task.delete()

        return redirect("crud_app:task_list_view")
