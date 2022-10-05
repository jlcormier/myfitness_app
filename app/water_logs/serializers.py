from rest_framework import serializers
from water_logs.models import Water


class WaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Water
        fields = ('id', 'date', 'time', 'water_amount')
