
from django.db import models
from datetime import datetime, date

from decimal import *

class Foodlog(models.Model):
    
    date = models.DateField(null=False, blank=False, auto_now=False, auto_now_add=False, default= date.today)
    time = models.TimeField(null=True, blank=True, auto_now=False, auto_now_add=False, default=("%H:%M"))
    number_servings = models.DecimalField(max_digits=3, decimal_places=2, null=False, blank=False)