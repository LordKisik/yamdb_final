from django.contrib.auth.models import AbstractUser
from django.db import models

from .validators import username_validation


class User(AbstractUser):
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'

    ROLE_CHOICE = (
        (USER, 'User'),
        (MODERATOR, 'Moderator'),
        (ADMIN, 'Admin'),
    )

    username = models.CharField(
        max_length=150,
        unique=True,
        blank=False,
        null=False,
        validators=[username_validation]
    )

    email = models.EmailField(
        max_length=254,
        unique=True,
        blank=False,
        null=False
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICE,
        default='user',
        blank=True
    )

    bio = models.TextField(
        blank=True
    )

    first_name = models.CharField(
        max_length=150,
        blank=True
    )

    last_name = models.CharField(
        max_length=150,
        blank=True
    )

    confirmation_code = models.CharField(
        max_length=255,
        null=True,
        blank=False,
        default='XXXXX'
    )

    class Meta:
        ordering = ('id',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username

    @property
    def is_admin(self):
        return self.role == self.ADMIN or self.is_superuser

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR

    @property
    def is_user(self):
        return self.role == self.USER
