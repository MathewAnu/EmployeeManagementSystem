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

