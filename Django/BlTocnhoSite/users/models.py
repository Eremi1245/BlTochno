from django.db import models
from django.contrib.auth.models import AbstractUser



class BlTochnoUser(AbstractUser):
    age=models.PositiveIntegerField(
        verbose_name='Возраст',
        blank=True,
        default=99
    )