from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.base_user import BaseUserManager


class UserManagers(UserManager):
    pass


class User(AbstractUser):
    objects = UserManagers()
