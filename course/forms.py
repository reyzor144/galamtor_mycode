from .models import Task
from django.forms import ModelForm, TextInput, Textarea


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'preview', 'task_text', 'tests']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название задачи'
            }),
            'preview': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс задачи'
            }),
            'task_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст задачи'
            }),
            'tests': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Тест задачи'
            }),
        }

# class TaskSendForm(ModelForm):
#     class Meta:
#         model = Task
#         fields = ['parcel_code', 'preview', 'task_text']
#
#         widgets = {
#             'title': TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Название задачи'
#             }),
#             'preview': TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Анонс задачи'
#             }),
#             'task_text': Textarea(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Текст задачи'
#             })
#         }
