from django.http import Http404
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Task
from .forms import TaskForm


def courses_home(request, task_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    # tasks = Task.objects.all()
    tasks = Task.objects.all()
    cur_task = tasks[0]
    cur_task = Task.objects.get(id=task_id)

    return render(request, 'courses_main.html', {'tasks': tasks, 'cur_task': cur_task})


def my_courses(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return render(request, 'my_courses.html')


def create(request):
    if not request.user.type == "TEACHER":
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Неверная форма задачи'

    form = TaskForm

    tasks = {
        'form': form,
        'error': error
    }
    return render(request, 'create.html', tasks)
