# Generated by Django 3.1.2 on 2020-10-31 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Title')),
                ('task_text', models.TextField(default='Task text', verbose_name='Text')),
                ('preview', models.CharField(max_length=250, verbose_name='Анонс задания')),
            ],
        ),
    ]
