from django.urls import path, include
from . import views

app_name = 'course'
urlpatterns = [
    path('<int:task_id>/', views.courses_home, name='courses_home'),
    path('create', views.create, name='create'),
    path('my_courses', views.my_courses, name='my_courses'),
    path('<int:task_id>/create_send', views.create_send, name='create_send'),
]
