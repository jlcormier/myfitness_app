from django.db import models
from datetime import datetime, date

from decimal import *

class Weight(models.Model):
    
    date = models.DateField(null=False, blank=False, auto_now=False, auto_now_add=False, default= date.today)
    time = models.TimeField(null=True, blank=True, auto_now=False, auto_now_add=False, default=("%H:%M"))
    weight = models.DecimalField(max_digits=4, decimal_places=1, null=False, blank=False)