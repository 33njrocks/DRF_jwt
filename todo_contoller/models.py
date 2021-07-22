from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
import jwt
import datetime
from _datetime import timedelta
from django.conf import settings
# Create your models here.

class User(AbstractUser):
    username=None               # while logging in admin panel django asks username by default . We do not want 
                                #username so username = None  
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)
    roles = models.CharField(max_length=100)
    password = models.CharField(max_length=20)

    objects = UserManager()

    USERNAME_FIELD = 'email'  # Instead of username we want admin to login by email id.
    REQUIRED_FIELDS = []


class Student(models.Model):
    name = models.CharField(max_length=50)
    roll_no = models.IntegerField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)