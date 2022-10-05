import datetime
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from food_logs.models import Foodlog
from food_logs.serializers import FoodlogSerializer
from rest_framework.decorators import api_view

# Create your views here.
# def index(request):
#     return render(request, "tutorials/index.html")

def index(request):
    print("------------------------- I AM HERE")
    queryset = Foodlog.objects.filter(date='enter log date')
    return render(request, "food_logs/index.html", {'food_logs': queryset})


class index(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'food_logs/index.html'

    def get(self, request):
        queryset = Foodlog.objects.filter(date='enter log date')
        return Response({'food_logs': queryset})


class list_all_food_logs(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'food_logs/foodlog_list.html'

    def get(self, request):
        queryset = Foodlog.objects.all()
        return Response({'food_logs': queryset})


@api_view(['GET', 'POST', 'DELETE'])
def foodlog_list(request):
    if request.method == 'GET':
        food_logs = Foodlog.objects.all()

        date = request.GET.get('date', None)
        if date is not None:
            food_logs = food_logs.filter(date__icontains=date)

        foodlog_serializer = FoodlogSerializer(food_logs, many=True)
        return JsonResponse(foodlog_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        foodlog_data = JSONParser().parse(request)
        foodlog_serializer = FoodlogSerializer(data=foodlog_data)
        if foodlog_serializer.is_valid():
            foodlog_serializer.save()
            return JsonResponse(foodlog_serializer.data,
                                status=status.HTTP_201_CREATED)
        return JsonResponse(foodlog_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Foodlog.objects.all().delete()
        return JsonResponse(
            {
                'message':
                '{} Food logs were deleted successfully!'.format(count[0])
            },
            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'PUT'])
def foodlog_detail(request, pk):
    try:
        foodlog = Foodlog.objects.get(pk=pk)
    except Foodlog.DoesNotExist:
        return JsonResponse({'message': 'The log does not exist'},
                            status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        foodlog_serializer = FoodlogSerializer
        (foodlog)
        return JsonResponse(foodlog_serializer.data)
    elif request.method == 'POST':
        foodlog_data = JSONParser().parse(request)
        foodlog_serializer = FoodlogSerializer(data=foodlog_data)
        if foodlog_serializer.is_valid():
            foodlog_serializer.save()
            return JsonResponse(foodlog_serializer.data,
                                status=status.HTTP_201_CREATED)
        return JsonResponse(foodlog_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        foodlog_data = JSONParser().parse(request)
        foodlog_serializer = FoodlogSerializer(foodlog, data=foodlog_data)
        if foodlog_serializer.is_valid():
            foodlog_serializer.save()
            return JsonResponse(foodlog_serializer.data)
        return JsonResponse(foodlog_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def foodlog_list_published(request):
    food_logs = Foodlog.objects(published=True)

    if request.method == 'GET':
        foodlog_serializer = FoodlogSerializer(food_logs, many=True)
        return JsonResponse(foodlog_serializer.data, safe=False)