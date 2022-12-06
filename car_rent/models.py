from django.db import models
import uuid
# Create your models here.
class User (models.Model):

    user_name = models.CharField(max_length=20)
    account = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    birthday = models.DateField()

    SEX = (
        ('m', 'Male'),
        ('f', 'Female'),
        ('n', 'None'),
    )

    sex = models.CharField(
        max_length=1,
        choices=SEX,
        default='m',
    )
    telephone = models.IntegerField()
    address = models.CharField(max_length=100)