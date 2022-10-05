from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from water_logs.models import Water
from water_logs.serializers import WaterSerializer
from rest_framework.decorators import api_view

# Create your views here.
# def index(request):
#     return render(request, "tutorials/index.html")

def index(request):
    print("------------------------- I AM HERE")
    queryset = Water.objects.filter(date='enter log date')
    return render(request, "water_logs/index.html", {'water_logs': queryset})


class index(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'water_logs/index.html'

    def get(self, request):
        queryset = Water.objects.filter(date='enter log date')
        return Response({'water_logs': queryset})


class list_all_water_logs(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'water_logs/water_list.html'

    def get(self, request):
        queryset = Water.objects.all()
        return Response({'water_logs': queryset})


@api_view(['GET', 'POST', 'DELETE'])
def water_list(request):
    if request.method == 'GET':
        water_logs = Water.objects.all()

        date = request.GET.get('date', None)
        if date is not None:
            water_logs = water_logs.filter(date__icontains=date)

        water_serializer = WaterSerializer(water_logs, many=True)
        return JsonResponse(water_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        water_data = JSONParser().parse(request)
        water_serializer = WaterSerializer(data=water_data)
        if water_serializer.is_valid():
            water_serializer.save()
            return JsonResponse(water_serializer.data,
                                status=status.HTTP_201_CREATED)
        return JsonResponse(water_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Water.objects.all().delete()
        return JsonResponse(
            {
                'message':
                '{} Food logs were deleted successfully!'.format(count[0])
            },
            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'PUT'])
def water_detail(request, pk):
    try:
        water = Water.objects.get(pk=pk)
    except Water.DoesNotExist:
        return JsonResponse({'message': 'The log does not exist'},
                            status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        water_serializer = WaterSerializer
        (Water)
        return JsonResponse(water_serializer.data)
    elif request.method == 'POST':
        water_data = JSONParser().parse(request)
        water_serializer = WaterSerializer(data=water_data)
        if water_serializer.is_valid():
            water_serializer.save()
            return JsonResponse(water_serializer.data,
                                status=status.HTTP_201_CREATED)
        return JsonResponse(water_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        water_data = JSONParser().parse(request)
        water_serializer = WaterSerializer(Water, data=water_data)
        if water_serializer.is_valid():
            water_serializer.save()
            return JsonResponse(water_serializer.data)
        return JsonResponse(water_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def water_list_published(request):
    water_logs = Water.objects(published=True)

    if request.method == 'GET':
        water_serializer = WaterSerializer(water_logs, many=True)
        return JsonResponse(water_serializer.data, safe=False)