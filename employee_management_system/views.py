from django.http import JsonResponse
from .serializers import EmployeeSerializer, TeamSerializer, TeamEmployeeSerializer, TeamLeaderSerializer, WorkArrangementSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
import employee_management_system.helper_functions as hf


@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def employee_list(request, req_emp_name=None):
    """
    To perform CRUD for model Employee
    :param request:
    :param req_emp_name: employee namme
    :return: status of the operation
    """
    if request.method == 'GET':
        if req_emp_name is None:
            employees_list = Employee.objects.all()
            obj_ser = EmployeeSerializer(employees_list, many=True)
        else:
            employees_list = Employee.objects.get(emp_name=req_emp_name)
            obj_ser = EmployeeSerializer(employees_list)
        if obj_ser is not None:
            return JsonResponse({'Employee': obj_ser.data}, status=status.HTTP_200_OK)
        else:
            return JsonResponse(status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'POST':
        obj_ser = EmployeeSerializer(data=request.data)
        if obj_ser.is_valid():
            obj_ser.save()
            return Response(obj_ser.data, status=status.HTTP_201_CREATED)
    if request.method == 'DELETE':
        if req_emp_name is not None:
            emp_chosen = Employee.objects.get(team_name=req_emp_name)
            if emp_chosen is not None:
                emp_chosen.delete()
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == 'PUT':
        try:
            emp_chosen = Employee.objects.get(team_name=req_emp_name)
        except Employee.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        obj_ser = EmployeeSerializer(emp_chosen, data=request.data)
        if obj_ser.is_valid():
            obj_ser.save()
            return Response(obj_ser.data)
    return Response(obj_ser.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def team_list(request, req_team_name=None):
    """
    To perform CRUD for model Team
    :param request:
    :param req_team_name: employee name
    :return: status of the operation
    """
    if request.method == 'GET':
        if req_team_name is None:
            teams_list = Team.objects.all()
            obj_ser = TeamSerializer(teams_list, many=True)
            return JsonResponse({'Team': obj_ser.data})
        else:
            teams_list = Team.objects.get(team_name=req_team_name)
            obj_ser = TeamSerializer(teams_list)
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
    if request.method == 'PUT':
        try:
            team_chosen = Team.objects.get(team_name=req_team_name)
        except Team.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        obj_ser = TeamSerializer(team_chosen, data=request.data)
        if obj_ser.is_valid():
            obj_ser.save()
            return Response(obj_ser.data)
        return Response(obj_ser.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def team_employee_list(request, req_emp_name=None):
    """
    To perform CRUD for model Team Employee
    :param request:
    :param req_emp_name: employee name
    :return: status of the operation
    """
    if request.method == 'GET':
        team_employees_list = TeamEmployee.objects.all()
        obj_ser = TeamEmployeeSerializer(team_employees_list, many=True)
        return JsonResponse({'TeamEmployee': obj_ser.data})
    if request.method == 'POST':
        obj_ser = TeamEmployeeSerializer(data=request.data)
        if obj_ser.is_valid():
            obj_ser.save()
            return Response(obj_ser.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        if req_emp_name is not None:
            emp_chosen = TeamEmployee.objects.get(team_name=req_emp_name)
            if emp_chosen is not None:
                emp_chosen.delete()
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == 'PUT':
        try:
            team_emp_chosen = TeamEmployee.objects.get(team_name=req_emp_name)
        except TeamEmployee.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        obj_ser = TeamEmployeeSerializer(team_emp_chosen, data=request.data)
        if obj_ser.is_valid():
            obj_ser.save()
            return Response(obj_ser.data)
        return Response(obj_ser.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def team_leader_list(request, req_emp_name=None):
    """
    To perform CRUD for model TeamLeader
    :param request:
    :param req_emp_name: employee name
    :return: status of the operation
    """
    if request.method == 'GET':
        team_leaders_list = TeamLeader.objects.all()
        obj_ser = TeamLeaderSerializer(team_leaders_list, many=True)
        return JsonResponse({'TeamLeader': obj_ser.data})
    if request.method == 'POST':
        obj_ser = TeamLeaderSerializer(data=request.data)
        if obj_ser.is_valid():
            obj_ser.save()
            return Response(obj_ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
    if request.method == 'DELETE':
        if req_emp_name is not None:
            emp_chosen = TeamLeader.objects.get(team_name=req_emp_name)
            if emp_chosen is not None:
                emp_chosen.delete()
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == 'PUT':
        try:
            team_lead_chosen = TeamLeader.objects.get(team_name=req_emp_name)
        except TeamLeader.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        obj_ser = TeamLeaderSerializer(team_lead_chosen, data=request.data)
        if obj_ser.is_valid():
            obj_ser.save()
            return Response(obj_ser.data)
        return Response(obj_ser.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def work_arragement_list(request, req_wa_percent=None):
    """
    To perform CRUD for model WorkArrangement
    :param request:
    :param req_wa_percent: working time in percentage
    :return: status of operation
    """
    if request.method == 'GET':
        work_arrangements_list = WorkArrangement.objects.all()
        obj_ser = WorkArrangementSerializer(work_arrangements_list, many=True)
        return JsonResponse({'WorkArrangement': obj_ser.data})
    if request.method == 'POST':
        obj_ser = TeamLeaderSerializer(data=request.data)
        if obj_ser.is_valid():
            obj_ser.save()
            return Response(obj_ser.data, status=status.HTTP_201_CREATED)
    if request.method == 'DELETE':
        if req_wa_percent is not None:
            wa_chosen = Team.objects.get(team_name=req_wa_percent)
            if wa_chosen is not None:
                wa_chosen.delete()
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == 'PUT':
        try:
            wa_chosen = WorkArrangement.objects.get(team_name=req_wa_percent)
        except WorkArrangement.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        obj_ser = WorkArrangementSerializer(wa_chosen, data=request.data)
        if obj_ser.is_valid():
            obj_ser.save()
            return Response(obj_ser.data)
        return Response(obj_ser.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def employee_salary_list(request, req_emp_name=None):
    """
    To calculate the salary of employees
    :param request:
    :param req_emp_name: employee name
    :return: status of operation
    """
    if request.method == 'GET':
        if req_emp_name is None:
            emp_salary_list = {}
            emp_list = Employee.objects.all()
            for emp in emp_list:
                work_percent = 0
                for w_arrangement in emp.emp_work_arrangement.all():
                    work_percent += w_arrangement.work_time_percentange
                additional_pay_percentage = 0
                team_leader_obj = TeamLeader.objects.all().filter(emp_name=emp.id)
                if len(team_leader_obj) != 0:
                    pass
                    additional_pay_percentage = TeamLeader.additional_pay_percentage
                emp_salary_list[emp.emp_name] = hf.calc_salary(emp.emp_hourly_rate, work_percent, additional_pay_percentage)
            return JsonResponse({'EmployeeSalary': emp_salary_list})
        else:
            emp_salary_list = {}
            emp = Employee.objects.get(emp_name=req_emp_name)
            work_percent = 0
            for w_arrangement in emp.emp_work_arrangement.all():
                work_percent += w_arrangement.work_time_percentange
            additional_pay_percentage = 0
            team_leader_obj = TeamLeader.objects.all().filter(emp_name=emp.id)
            if len(team_leader_obj) != 0:
                additional_pay_percentage = TeamLeader.additional_pay_percentage
            emp_salary_list[emp.emp_name] = hf.calc_salary(emp.emp_hourly_rate, work_percent,
                                                               additional_pay_percentage)
            return JsonResponse({'EmployeeSalary': emp_salary_list})
    return Response(status=status.HTTP_400_BAD_REQUEST)

