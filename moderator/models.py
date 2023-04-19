from django.db import models
from django.contrib.auth.models import AbstractUser

class MainUser(AbstractUser):
    phone_number = models.CharField(max_length=10, verbose_name='Telefon raqam')

    def __str__(self):
        return f"{self.username} ({self.last_name} {self.first_name})"

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Userlar'
