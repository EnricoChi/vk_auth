from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from landing.utils import get_vk_friends
from .managers import AccountManager


class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        'Email')
    first_name = models.CharField(
        'Имя', max_length=50)
    social_pict = models.URLField(
        'Фото', blank=True)
    social_id = models.CharField(
        'VK id', max_length=255, unique=True)

    date_joined = models.DateTimeField(
        'Зарегистрирован', auto_now_add=True)
    is_active = models.BooleanField(
        'Аккаунт активен', default=True)
    is_verified = models.BooleanField(
        'Почта подтверждена', default=False)
    is_staff = models.BooleanField(
        'В штате', default=False)

    objects = AccountManager()

    def __str__(self):
        return self.social_id

    @property
    def get_friends(self):
        friends_list = get_vk_friends(self)['response']['items']

        return friends_list

    USERNAME_FIELD = 'social_id'
