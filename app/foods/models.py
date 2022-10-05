
from django.db import models

from decimal import *

class Food(models.Model):
    
    food_desc = models.CharField(max_length=30, unique=True, null=False, blank=False)
    calories = models.DecimalField(max_digits=5, decimal_places=1, null=False, blank=False)
    protein_g = models.DecimalField(max_digits=4, decimal_places=1, null=False, blank=False)
    carbs_g = models.DecimalField(max_digits=4, decimal_places=1, null=False, blank=False)
    fat_g = models.DecimalField(max_digits=4, decimal_places=1, null=False, blank=False)
    sugar_g = models.DecimalField(max_digits=4, decimal_places=1, null=False, blank=False)
    gm_wt_1 = models.DecimalField(max_digits=4, decimal_places=1, null=False, blank=False)
    wt_desc_1 = models.CharField(max_length=50, null=False, blank=False)
    gm_wt_2 = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True, default= '')
    wt_desc_2= models.CharField(max_length=50, null=False, blank=False)