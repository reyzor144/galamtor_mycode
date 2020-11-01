from django.urls import path, include
from . import views

app_name = 'course'
urlpatterns = [
    path('', views.courses_home, name='courses_home'),
    path('<int:task_id>/', views.view_task, name='cur_course'),
    path('<int:task_id>/create_send', views.create_send, name='create_send'),
    path('create', views.create, name='create'),
    path('my_courses', views.my_courses, name='my_courses'),
]
