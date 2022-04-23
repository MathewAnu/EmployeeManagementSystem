from django.db import models


class Team(models.Model):
    team_name = models.CharField(max_length=20, primary_key=True)

    def __str__(self):
        return self.team_name


class Employee(models.Model):
    emp_name = models.CharField(max_length=50, default=None)
    emp_team_name = models.ForeignKey(Team, on_delete=models.SET_NULL, default=None, null=True, related_name='%(class)s')
    emp_hourly_rate = models.FloatField(default=15)

    def __str__(self):
        return self.emp_name

    class Meta:
        abstract = True


class TeamEmployee(Employee):
    def __str__(self):
        return self.emp_name


class TeamLeader(Employee):
    additional_pay_percentage = 10

    def __str__(self):
        return self.emp_name




