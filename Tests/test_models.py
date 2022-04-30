from django.test import TestCase
from employee_management_system.models import Employee, WorkArrangement, TeamEmployee, TeamLeader, Team


class TestModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.w_a_obj = WorkArrangement.objects.create(work_time_percentange=50, work_type="Part-time")
        cls.emp_obj = Employee.objects.create(emp_name="Test Employee", emp_hourly_rate=10)
        cls.emp_obj.emp_work_arrangement.set([cls.w_a_obj.pk])
        cls.team_obj = Team.objects.create(team_name="TestTeam")
        cls.team_emp_obj = TeamEmployee.objects.create(emp_name=cls.emp_obj, emp_team_name=cls.team_obj)
        cls.emp_lead_obj = Employee.objects.create(emp_name="Test Leader", emp_hourly_rate=10)
        cls.emp_lead_obj.emp_work_arrangement.set([cls.w_a_obj.pk])
        cls.team_lead_obj = TeamLeader.objects.create(emp_name=cls.emp_lead_obj, emp_team_name=cls.team_obj)


class TestWorkArrangement(TestModel):
    def test_employee_str(self):
        self.assertEqual(str(self.w_a_obj), "50")


class TestEmployee(TestModel):
    def test_employee_str(self):
        self.assertEqual(str(self.emp_obj), "Test Employee")


class TestTeam(TestModel):
    def test_team_str(self):
        self.assertEqual(str(self.team_obj), "TestTeam")


class TestTeamEmployee(TestModel):
    def test_team_employee_str(self):
        self.assertEqual(str(self.team_emp_obj), "Test Employee")


class TestLeaderEmployee(TestModel):
    def test_team_leader_str(self):
        self.assertEqual(str(self.team_lead_obj), "Test Leader")


