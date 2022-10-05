from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from weight_logs.models import Weight
from weight_logs.serializers import WeightSerializer
from rest_framework.decorators import api_view


def index(request):
    print("------------------------- I AM HERE")
    queryset = Weight.objects.filter(date='enter log date')
    return render(request, "weight_logs/index.html", {'weight_logs': queryset})


class index(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'weight_logs/index.html'

    def get(self, request):
        queryset = Weight.objects.filter(date='enter log date')
        return Response({'weight_logs': queryset})


class list_all_weight_logs(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'weight_logs/weight_list.html'

    def get(self, request):
        queryset = Weight.objects.all()
        return Response({'weight_logs': queryset})


@api_view(['GET', 'POST', 'DELETE'])
def weight_list(request):
    if request.method == 'GET':
        weight_logs = Weight.objects.all()
        date = request.GET.get('date', None)
        if date is not None:
            weight_logs = weight_logs.filter(date__icontains=date)

        weight_serializer = WeightSerializer(weight_logs, many=True)
        return JsonResponse(weight_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        weight_data = JSONParser().parse(request)
        weight_serializer = WeightSerializer(data=weight_data)
        if weight_serializer.is_valid():
            weight_serializer.save()
            return JsonResponse(weight_serializer.data,
                                status=status.HTTP_201_CREATED)
        return JsonResponse(weight_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Weight.objects.all().delete()
        return JsonResponse(
            {
                'message':
                '{} Food logs were deleted successfully!'.format(count[0])
            },
            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'PUT'])
def weight_detail(request, pk):
    try:
        weight = Weight.objects.get(pk=pk)
    except Weight.DoesNotExist:
        return JsonResponse({'message': 'The log does not exist'},
                            status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        weight_serializer = WeightSerializer
        (weight)
        return JsonResponse(weight_serializer.data)
    elif request.method == 'POST':
        weight_data = JSONParser().parse(request)
        weight_serializer = WeightSerializer(data=weight_data)
        if weight_serializer.is_valid():
            weight_serializer.save()
            return JsonResponse(weight_serializer.data,
                                status=status.HTTP_201_CREATED)
        return JsonResponse(weight_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        weight_data = JSONParser().parse(request)
        weight_serializer = WeightSerializer(Weight, data=weight_data)
        if weight_serializer.is_valid():
            weight_serializer.save()
            return JsonResponse(weight_serializer.data)
        return JsonResponse(weight_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def weight_list_published(request):
    weight_logs = Weight.objects(published=True)

    if request.method == 'GET':
        weight_serializer = WeightSerializer(weight_logs, many=True)
        return JsonResponse(weight_serializer.data, safe=False)