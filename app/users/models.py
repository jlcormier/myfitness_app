#type: ignore
from django.contrib.auth.models import User
from django.db import models


class User (models.Model):
        
    username = models.CharField(max_length=8, unique=True, null=False, blank=False)
    password = models.CharField(max_length=15, null=False, blank=False)
    email = models.CharField(max_length=50, unique=True, null=False, blank=False)
    firstname = models.CharField(max_length=30, null=True, blank=True, default = '')

    age = models.CharField(max_length=2, null=True, blank=True, default='')

    MALE = 1
    FEMALE = 2
    NON_BINARY = 3
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (NON_BINARY, 'Non-Binary'),
    ]
    gender =  models.PositiveSmallIntegerField(choices=GENDER_CHOICES, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    zip = models.CharField(max_length=5, null=True, blank=True)
