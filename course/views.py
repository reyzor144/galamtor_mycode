from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


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
