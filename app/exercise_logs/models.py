
from django.db import models
from datetime import datetime, date, time

from decimal import *
getcontext().prec = 1

class Exercise(models.Model):
    
    date = models.DateField(blank=True, auto_now=False, auto_now_add=False, default=date.today)
    time = models.TimeField(null=True, blank=True, auto_now=False, auto_now_add=False, default=("%H:%M"))
    type = models.CharField(max_length=50, blank=True, default='')
    calories_per_hr = models.DecimalField(max_digits=5, decimal_places=1, blank=True, default='')
    hours = models.DecimalField(max_digits=3, decimal_places=1, blank=True, default='')