from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'age', 'gender', 'city', 'zip', 'start_weight_lbs', 'goal_weight_lbs', 'water_goal_oz', 'exercise_goal_hrs', 'calories_goal', 'protein_goal_g', 'carbs_goal_g', 'fat_goal_g')
