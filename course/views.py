from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from datetime import datetime
from .models import Task, Send
from .forms import TaskForm
from .testing_staff import pycheck
import account.models


def courses_home(request):
    tasks = Task.objects.all()

    return render(request, 'courses_main.html', {'tasks': tasks})


def my_courses(request):
    return render(request, 'my_courses.html')


def create(request):
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


def view_task(request, task_id):
    try:
        cur_task = Task.objects.get(id=task_id)
    except:
        raise Http404("Page doesn't exist")
    latest_sends_list = cur_task.send_set.order_by('-id')[:10]
    return render(request, 'sample_task.html', {'task': cur_task, 'list': latest_sends_list})


def create_send(request, task_id):
    try:
        cur_task = Task.objects.get(id=task_id)
    except:
        raise Http404("Page doesn't exist")

    tmp = cur_task.send_set.create(runtime=0, verdict="HZ", code=request.POST['user_code'], last_test=1, date=datetime.now())
    TL = 2
    is_python = True
    if is_python:
        [tmp.verdict, tmp.last_test, tmp.runtime] = pycheck.pytest(tmp.code, cur_task.tests.split(';')[::2],
                                                                cur_task.tests.split(';')[1::2], TL).split(" ")
        tmp.lang = "Python3"
    else:
        [tmp.verdict, tmp.last_test, tmp.runtime] = pycheck.cpptest(tmp.code, cur_task.tests.split(';')[::2], cur_task.tests.split(';')[1::2], TL).split(" ")
        tmp.lang = "c++"
    tmp.save()

    return HttpResponseRedirect(reverse("course:cur_course", args=(cur_task.id,)))
