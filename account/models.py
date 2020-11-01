from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, Group
from course.models import Task
from django.utils.translation import gettext_lazy as _
from django.urls import reverse



class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None, name=None, surname=None, third_name=None, school=None,
                    birthday=None):
        if not email:
            return ValueError("Users must have an email address")
        if not username:
            return ValueError("Users must have an username")
        if not name:
            return ValueError("Users must have a name")
        if not surname:
            return ValueError("Users must have a surname")
        if not third_name:
            return ValueError("Users must have a third_name")
        if not school:
            return ValueError("Users must have a school")
        if not birthday:
            return ValueError("Users must have a birthday")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            name=name,
            surname=surname,
            third_name=third_name,
            school=school,
            birthday=birthday,
        )

        self.groups.add(Group.objects.get(name='student'))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password, name, surname, third_name, school, birthday):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
            name=name,
            surname=surname,
            third_name=third_name,
            school=school,
            birthday=birthday,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):

    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)

    name = models.CharField(verbose_name="Имя", max_length=40)
    surname = models.CharField(verbose_name="Фамилия", max_length=40)
    third_name = models.CharField(verbose_name="Отчество", max_length=40)

    birthday = models.DateField(verbose_name="Дата рождения")
    school = models.CharField(verbose_name="Образовательная организация", max_length=250)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name', 'surname', 'third_name', 'school', 'birthday']

    object = MyAccountManager()

    class Types(models.TextChoices):
        STUDENT = "STUDENT", "Student"
        TEACHER = "TEACHER", "Teacher"

    # Какой тип пользователя?
    type = models.CharField(_('Type'), max_length=50, choices=Types.choices, default=Types.STUDENT)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

    def __str__(self):
        return self.email + ", " + self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class StudentManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=Account.Types.STUDENT)


class Student(Account):
    objects = StudentManager()



    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = Account.Types.STUDENT
        return super().save(*args, **kwargs)


class TeacherManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=Account.Types.TEACHER)


class Teacher(Account):
    objects = TeacherManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = Account.Types.TEACHER
        return super().save(*args, **kwargs)
