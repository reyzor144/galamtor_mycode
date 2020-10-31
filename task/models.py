from django.db import models
from account.models import Account


# class MyTaskManager(models.Model):
#     def create_task(self, task_name, text, preview=None, samples_value=0):
#         if not task_name:
#             return ValueError("Task must have a name")
#         if not text:
#             return ValueError("Task must have a text")
#
#         task = self.model(
#             task_name=task_name,
#             text=text,
#             preview=preview,
#             samples_value=samples_value,
#         )
#
#         task.save(using=self._db)
#         return task


class Task(models.Model):
    task_name = models.CharField(max_length=250, verbose_name='Название')
    text = models.TextField(verbose_name="Текст задания")
    preview = models.CharField(max_length=250, verbose_name="Анонс задания")

    samples = []

    samples_value = models.BigIntegerField(verbose_name="Сколько будет примеров", default=0)

    # students = models.ManyToManyField(Account)

    def __str__(self):
        return self.task_name + ", " + self.preview

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


# def add_user(task, student):
#     task.students.add(student)
