from rest_framework import serializers
from foods.models import Food


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ('id', 'food_desc', 'calories', 'protein_g', 'carbs_g',
                  'fat_g', 'sugar_g', 'gm_wt_1', 'wt_desc_1', 'gm_wt_2', 'wt_desc_2')