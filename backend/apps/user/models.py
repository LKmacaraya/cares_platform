from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    user_id = models.CharField(max_length=20, unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    is_resident_of_cebu = models.BooleanField(default=False)
    lgu = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    avatar = models.ImageField(upload_to='users/avatar/', null=True, blank=True)
    is_rhu = models.BooleanField(default=False)
    is_private = models.BooleanField(default=False)

    # Check if the user logged in for the first time
    is_first_login = models.BooleanField(default=True)
    plain_password = models.CharField(max_length=128, null=True, blank=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['last_name', 'first_name']

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'.strip()

    def __str__(self):
        return self.username