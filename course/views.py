from django.http import Http404
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime, timezone
from .models import Task, Send
from .forms import TaskForm
from .testing_staff import pycheck


def courses_home(request, task_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    # tasks = Task.objects.all()
    tasks = Task.objects.all()
    # cur_task = tasks[0]
    curr_task = Task.objects.get(id=task_id)
    latest_sends_list = curr_task.send_set.order_by('-id')[:10]
    return render(request, 'courses_main.html', {'tasks': tasks, 'cur_task': curr_task, 'list': latest_sends_list})


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

    return HttpResponseRedirect(reverse("course:courses_home", args=(cur_task.id,)))
