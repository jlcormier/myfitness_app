from rest_framework import serializers
from food_logs.models import Foodlog


class FoodlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foodlog
        fields = ('id', 'date', 'time', 'number_servings')
