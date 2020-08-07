from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    name=models.CharField(max_length = 100)
    phone_number=models.CharField(max_length=11)
    communication_purpose=models.BooleanField(default=False)
    understanding_purpose=models.BooleanField(default=False)
    teacher=models.BooleanField(default=False)
    parent=models.BooleanField(default=False)
    other_purpose=models.BooleanField(default=False)