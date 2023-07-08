import json

from django.test import TestCase
from rest_framework import status


class TestView(TestCase):
    def set_up_test_data(self):
        pass

    def test_team_view(self):
        data = {"team_name": "TestTeam"}
        response = self.client.post('/employee_management_system/Team', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.get('/employee_management_system/Team', kwargs={"team_name": "TestTeam"})
        self.assertEqual(json.loads(response.content), {"Team": [{"team_name": "TestTeam"}]})

    #def test_work_arrangement_view(self):
     #   data = {"work_time_percentange": 50, "work_type": "Part-time"}
      #  response = self.client.post('/employee_management_system/WorkArrangement', data)
       # self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    # response = self.client.get('/employee_management_system/Team', kwargs={"team_name": "TestTeam"})
    # self.assertEqual(json.loads(response.content), {"Team": [{"team_name": "TestTeam"}]})

    def test_employee_view(self):
        data = {"emp_name": "Test User", "emp_hourly_rate": 15.0, "emp_work_arrangement": {"id": [8, 9]}}
        response = self.client.post('/employee_management_system/Employee', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        #response = self.client.get('/employee_management_system/Team', kwargs={"team_name": "TestTeam"})
        #self.assertEqual(json.loads(response.content), {"Team": [{"team_name": "TestTeam"}]})
