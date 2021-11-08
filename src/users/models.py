from django.db import models

from django.contrib.auth.models import AbstractUser

from todo_app.models import Project


class User(AbstractUser):
    first_name = models.CharField(max_length=64, verbose_name='имя')
    last_name = models.CharField(max_length=64, verbose_name='фамилия')
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
        verbose_name='электронная почта'
    )
    project = models.ManyToManyField(Project, related_name='project_users')

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return f'{self.pk} | {self.last_name} {self.first_name}'
