from django.db import models
from datetime import datetime


class Task(models.Model):
    title = models.CharField(verbose_name='Название', max_length=60)

    task_text = models.TextField(verbose_name='Текст задания',)

    preview = models.CharField(max_length=250, verbose_name="Анонс задания")

    tests = models.TextField(verbose_name='Тесты')

    def __str__(self):
        return f'Задача: {self.title}'


class Send(models.Model):
    #account = models.ForeignKey('account.Account', on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    verdict = models.CharField(max_length=3, verbose_name='Verdict',)
    last_test = models.IntegerField(verbose_name='lt test',)
    code = models.TextField(verbose_name="code", default="code")
    lang = models.CharField(max_length=10, verbose_name='lang', default="python3")
    runtime = models.FloatField(verbose_name="time", default=0)
    date = models.DateField(verbose_name="date")

    def __str__(self):
        return f'date: {self.date}  id: {self.id}  lang: {self.lang}  verdict: {self.verdict}{self.last_test}  time: {self.runtime}'
