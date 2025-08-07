from django.db import models
from django.contrib.auth.models import AbstractBaseUser


# Create your models here.
class User(AbstractBaseUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('staff', 'Staff'),
        ('operator', 'Operator'),
    )
    email = models.EmailField(verbose_name="email", unique=True)
    username = models.CharField(max_length=150, unique=True, null=True, blank=True)
    is_email_verified = models.BooleanField(default=False)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='operator')

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

