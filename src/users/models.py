from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=64, verbose_name='имя')
    last_name = models.CharField(max_length=64, verbose_name='фамилия')
    email = models.CharField(
        primary_key=True,
        verbose_name='электронная почта'
    )

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
