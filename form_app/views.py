from django.shortcuts import render

TASKS = []


def create_task(request):
    task = request.GET.get('task')
    if task:
        TASKS.append(task)

    return render(
        request,
        'form_app/task_form.html',
        context={
            'tasks': TASKS
        }
    )
