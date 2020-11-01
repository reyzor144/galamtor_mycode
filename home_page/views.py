from django.shortcuts import render
from course.models import Task
from django.http import HttpResponse

# def homepage_view(request, *args, **kwargs):
#     print(request.user)
#     cur_html = open("templates/home.html", 'r')
#     return HttpResponse(cur_html)


def advanced_homepage_view(request, *args, **kwargs):
    tasks = Task.objects.all()
    st_task = tasks[0]

    return render(request, "home_page/home.html", {'st_task': st_task})
