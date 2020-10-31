from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.courses_home, name='courses_home'),
    path('create', views.create, name='create'),
    path('my_courses', views.my_courses, name='my_courses'),
]
