"""employee_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from employee_management_system import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee_management_system/Employee', views.employee_list),
    path('employee_management_system/Employee/<str:req_emp_name>', views.employee_list),
    path('employee_management_system/Salary', views.employee_salary_list),
    path('employee_management_system/Team/<str:req_team_name>', views.team_list),
    path('employee_management_system/Team', views.team_list),
    path('employee_management_system/TeamEmployee', views.team_employee_list),
    path('employee_management_system/TeamEmployee/<str:req_emp_name>', views.team_employee_list),
    path('employee_management_system/TeamLeader', views.team_leader_list),
    path('employee_management_system/TeamLeader/<str:req_emp_name>', views.team_leader_list),
    path('employee_management_system/WorkArrangement', views.work_arragement_list),
    path('employee_management_system/WorkArrangement/<int:req_wa_percent>', views.work_arragement_list)
]
