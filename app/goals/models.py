from django.db import models

#type: ignore

from tokenize import Ignore
from django.db import models
Ignore
class Goal(models.Model):

    title = models.CharField(max_length=70, blank=False, default='')
    start_weight_lbs = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True, default='')
    goal_weight_lbs = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True, default='')
    water_goal_oz = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True, default='')
    exercise_goal_hrs = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True, default='')
    calories_goal = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True, default='')
    protein_goal_g = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True, default='')
    carbs_goal_g = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True, default='')
    fat_goal_g = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True, default='')