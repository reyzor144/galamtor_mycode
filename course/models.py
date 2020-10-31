from django.db import models


class Task(models.Model):
    title = models.CharField(verbose_name='Title', max_length=60)

    task_text = models.TextField(verbose_name='Text', default='Task text')

    preview = models.CharField(max_length=250, verbose_name="Анонс задания")

    # task_answer = models.FileField()

    def __str__(self):
        return f'Задача: {self.title}'



