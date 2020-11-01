from django.shortcuts import render
from django.http import HttpResponse

# def homepage_view(request, *args, **kwargs):
#     print(request.user)
#     cur_html = open("templates/home.html", 'r')
#     return HttpResponse(cur_html)


def advanced_homepage_view(request, *args, **kwargs):
    return render(request, "home_page/home.html", {})
