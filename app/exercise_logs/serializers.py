from rest_framework import serializers
from exercise_logs.models import Exercise


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ('id', 'date', 'time', 'type', 'calories_per_hr', 'hours')
