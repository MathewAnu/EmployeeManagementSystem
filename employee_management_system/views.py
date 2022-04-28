from django.http import JsonResponse
from .serializers import EmployeeSerializer, TeamSerializer, TeamEmployeeSerializer, TeamLeaderSerializer, WorkArrangementSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *


@api_view(['GET', 'POST'])
def employee_list(request):
    if request.method == 'GET':
        employees_list = Employee.objects.all()
        obj_ser = EmployeeSerializer(employees_list, many=True)
        return JsonResponse({'Employee': obj_ser.data})
    if request.method == 'POST':
        obj_ser = EmployeeSerializer(data=request.data)
        if obj_ser.is_valid():
            obj_ser.save()
            return Response(obj_ser.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST', 'DELETE'])
def team_list(request, req_team_name=""):
    if request.method == 'GET':
        if req_team_name == "":
            teams_list = Team.objects.all()
            obj_ser = TeamSerializer(teams_list, many=True)
            return JsonResponse({'Team': obj_ser.data})
        else:
            teams_list = Team.objects.get(team_name=req_team_name)
            obj_ser = TeamSerializer(teams_list, many=True)
            return JsonResponse({'Team': obj_ser.data})
    if request.method == 'POST':
        obj_ser = TeamSerializer(data=request.data)
        if obj_ser.is_valid():
            obj_ser.save()
            return Response(obj_ser.data, status=status.HTTP_201_CREATED)
    if request.method == 'DELETE':
        team_chosen = Team.objects.get(team_name=req_team_name)
        team_chosen.delete()
        return Response(status=status.HTTP_201_CREATED)
    '''
    if request.method == 'PUT':
        team_chosen = Team.objects.get(team_name=req_team_name)
        obj_ser = TeamSerializer(data=request.data)
        if obj_ser.is_valid():
            obj_ser.save()
            return Response(obj_ser.data)
        return Response(obj_ser.errors, status=status.HTTP_400_BAD_REQUEST)'''


@api_view(['GET', 'POST'])
def team_employee_list(request):
    if request.method == 'GET':
        team_employees_list = TeamEmployee.objects.all()
        obj_ser = TeamEmployeeSerializer(team_employees_list, many=True)
        return JsonResponse({'TeamEmployee': obj_ser.data})
    if request.method == 'POST':
        obj_ser = TeamEmployeeSerializer(data=request.data)
        if obj_ser.is_valid():
            obj_ser.save()
            return Response(obj_ser.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def team_leader_list(request):
    if request.method == 'GET':
        team_leaders_list = TeamLeader.objects.all()
        obj_ser = TeamLeaderSerializer(team_leaders_list, many=True)
        return JsonResponse({'TeamLeader': obj_ser.data})
    if request.method == 'POST':
        obj_ser = TeamLeaderSerializer(data=request.data)
        if obj_ser.is_valid():
            obj_ser.save()
            return Response(obj_ser.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def work_arragement_list(request):
    if request.method == 'GET':
        work_arrangements_list = WorkArrangement.objects.all()
        obj_ser = WorkArrangementSerializer(work_arrangements_list, many=True)
        return JsonResponse({'WorkArrangement': obj_ser.data})
    if request.method == 'POST':
        obj_ser = TeamLeaderSerializer(data=request.data)
        if obj_ser.is_valid():
            obj_ser.save()
            return Response(obj_ser.data, status=status.HTTP_201_CREATED)
