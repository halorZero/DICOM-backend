from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatar', default='media/avatar/default.png')
    bio = models.TextField()
    sex = models.SmallIntegerField(default=0)
    level = models.SmallIntegerField(default=0)
