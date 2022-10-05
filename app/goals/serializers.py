from rest_framework import serializers
from goals.models import Goal


class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = ('id', 'start_weight_lbs', 'goal_weight_lbs', 'water_goal_oz', 'exercise_goal_hrs', 'calories_goal', 'protein_goal_g', 'carbs_goal_g', 'fat_goal_g')
