from django.db import models


class Task(models.Model):
    title = models.CharField(verbose_name='Название', max_length=60)

    task_text = models.TextField(verbose_name='Текст задания', default='Задание')

    preview = models.CharField(max_length=250, verbose_name="Анонс задания")

    tests = models.TextField(verbose_name='Тесты', default="")

    def __str__(self):
        return f'Задача: {self.title}'


class Send(models.Model):
    account = models.ForeignKey('account.Account', on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    verdict = models.CharField(max_length=3, verbose_name='Verdict')
    last_test = models.IntegerField(verbose_name='last test')

    def __str__(self):
        return f'{self.id}'
