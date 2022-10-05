import datetime
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from exercise_logs.models import Exercise
from exercise_logs.serializers import ExerciseSerializer
from rest_framework.decorators import api_view

# Create your views here.
# def index(request):
#     return render(request, "tutorials/index.html")

def index(request):
    print("------------------------- I AM HERE")
    queryset = Exercise.objects.filter(date='enter log date')
    return render(request, "exercise_logs/index.html", {'exercise_logs': queryset})


class index(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'exercise_logs/index.html'

    def get(self, request):
        queryset = Exercise.objects.filter(date='enter log date')
        return Response({'exercise_logs': queryset})


class list_all_exercise_logs(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'exercise_logs/exercise_list.html'

    def get(self, request):
        queryset = Exercise.objects.all()
        return Response({'exercise_logs': queryset})


@api_view(['GET', 'POST', 'DELETE'])
def exercise_list(request):
    if request.method == 'GET':
        exercise_logs = Exercise.objects.all()

        date = request.GET.get('date', None)
        if date is not None:
            exercise_logs = exercise_logs.filter(date__icontains=date)

        exercise_serializer = ExerciseSerializer(exercise_logs, many=True)
        return JsonResponse(exercise_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        exercise_data = JSONParser().parse(request)
        exercise_serializer = ExerciseSerializer(data=exercise_data)
        if exercise_serializer.is_valid():
            exercise_serializer.save()
            return JsonResponse(exercise_serializer.data,
                                status=status.HTTP_201_CREATED)
        return JsonResponse(exercise_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Exercise.objects.all().delete()
        return JsonResponse(
            {
                'message':
                '{} Exercise logs were deleted successfully!'.format(count[0])
            },
            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'PUT'])
def excerise_detail(request, pk):
    try:
        exercise = Exercise.objects.get(pk=pk)
    except Exercise.DoesNotExist:
        return JsonResponse({'message': 'The log does not exist'},
                            status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        exercise_serializer = ExerciseSerializer
        (exercise)
        return JsonResponse(exercise_serializer.data)
    elif request.method == 'POST':
        exercise_data = JSONParser().parse(request)
        exercise_serializer = ExerciseSerializer(data=exercise_data)
        if exercise_serializer.is_valid():
            exercise_serializer.save()
            return JsonResponse(exercise_serializer.data,
                                status=status.HTTP_201_CREATED)
        return JsonResponse(exercise_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        exercise_data = JSONParser().parse(request)
        exercise_serializer = ExerciseSerializer(exercise, data=exercise_data)
        if exercise_serializer.is_valid():
            exercise_serializer.save()
            return JsonResponse(exercise_serializer.data)
        return JsonResponse(exercise_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def exercise_list_published(request):
    exercise_logs = Exercise.objects(published=True)

    if request.method == 'GET':
        exercise_serializer = ExerciseSerializer(exercise_logs, many=True)
        return JsonResponse(exercise_serializer.data, safe=False)