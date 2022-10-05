from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from foods.models import Food
from foods.serializers import FoodSerializer
from rest_framework.decorators import api_view


def index(request):
    print("------------------------- I AM HERE")
    queryset = Food.objects.filter(food_desc='enter food name or description')
    return render(request, "foods/index.html", {'foods': queryset})


class index(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'foods/index.html'

    def get(self, request):
        queryset = Food.objects.filter(food_desc='enter food name or description')
        return Response({'foods': queryset})


class list_all_foods(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'foods/food_list.html'

    def get(self, request):
        queryset = Food.objects.all()
        return Response({'foods': queryset})


@api_view(['GET'])
def food_list(request):
    if request.method == 'GET':
        foods = Food.objects.all()
        food_desc = request.GET.get('food_desc', None)
        if food_desc is not None:
            foods = foods.filter(date__icontains=food_desc)

        food_serializer = FoodSerializer(foods, many=True)
        return JsonResponse(food_serializer.data, safe=False)
        # 'safe=False' for objects serialization


@api_view(['GET', 'POST', 'PUT'])
def Food_detail(request, pk):
    try:
        food = Food.objects.get(pk=pk)
    except Food.DoesNotExist:
        return JsonResponse({'message': 'The log does not exist'},
                            status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        food_serializer = FoodSerializer(food)
        return JsonResponse(food_serializer.data)
    

@api_view(['GET'])
def food_list_published(request):
    foods = Food.objects(published=True)

    if request.method == 'GET':
        food_serializer = FoodSerializer(foods, many=True)
        return JsonResponse(food_serializer.data, safe=False)