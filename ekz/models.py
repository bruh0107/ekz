from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    avatar = models.FileField(upload_to='avatars/', blank=True, null=True)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=150)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'avatar']

    def __str__(self):
        return self.username

