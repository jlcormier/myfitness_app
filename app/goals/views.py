import datetime
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from goals.models import Goal
from goals.serializers import GoalSerializer
from rest_framework.decorators import api_view

# Create your views here.
# def index(request):
#     return render(request, "goals/index.html")

class index(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'goals/index.html'


class goals_details(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'goals/goal_list.html'


@api_view(['GET', 'POST', 'PUT'])
def goal_detail(request, pk):
    try:
        goal = Goal.objects.get(pk=pk)
    except Goal.DoesNotExist:
        return JsonResponse({'message': 'The goal does not exist'},
                            status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        goal_serializer = GoalSerializer
        (goal)
        return JsonResponse(goal_serializer.data)
    elif request.method == 'POST':
        goal_data = JSONParser().parse(request)
        goal_serializer = GoalSerializer(data=goal_data)
        if goal_serializer.is_valid():
            goal_serializer.save()
            return JsonResponse(goal_serializer.data,
                                status=status.HTTP_201_CREATED)
        return JsonResponse(goal_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        goal_data = JSONParser().parse(request)
        goal_serializer = GoalSerializer(goal, data=goal_data)
        if goal_serializer.is_valid():
            goal_serializer.save()
            return JsonResponse(goal_serializer.data)
        return JsonResponse(goal_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def goal_detail_published(request):
    goals = Goal.objects(published=True)

    if request.method == 'GET':
        goals_serializer = GoalSerializer(goals)
        return JsonResponse(goals_serializer.data, safe=False)