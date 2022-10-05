from rest_framework import serializers
from weight_logs.models import Weight


class WeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weight
        fields = ('id', 'date', 'time', 'weight')
