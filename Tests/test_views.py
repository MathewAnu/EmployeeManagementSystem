from django.test import TestCase
from employee_management_system.models import Employee, WorkArrangement, TeamEmployee, TeamLeader, Team


class TestView(TestCase):
    def set_up_test_data(self):
        pass

    def test_employee_str(self):
        self.w_a = WorkArrangement.objects.create(work_time_percentange=50, work_type="Part-time")
        self.emp_obj = Employee.objects.create(emp_name="Test Employee", emp_hourly_rate=10)
        self.emp_obj.emp_work_arrangement.set([self.w_a.pk])
        self.assertEqual(str(self.emp_obj), "Test Employee")


