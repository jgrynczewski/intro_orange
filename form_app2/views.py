from django.shortcuts import render

TASKS = []


def create_task(request):
    task = request.POST.get('task')
    if task:
        TASKS.append(task)

    return render(
        request,
        'form_app2/task_form.html',
        context={
            'tasks': TASKS
        }
    )
