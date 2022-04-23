from django.db import models


class Team(models.Model):
    team_name = models.CharField(max_length=20, primary_key=True)

    def __str__(self):
        return self.team_name


class WorkArrangement(models.Model):
    work_percentage_options = ((100, 100), (75, 75), (50, 50), (25, 25))
    work_time_percentange = models.IntegerField(choices=work_percentage_options, default=100)
    if work_time_percentange == 100:
        work_type = models.CharField(max_length=15, editable=False, default="Full-time")
    else:
        work_type = models.CharField(max_length=15, editable=False, default="Part-time")

    def __str__(self):
        return str(self.work_time_percentange)


class Employee(models.Model):
    emp_name = models.CharField(max_length=50, default=None)
    emp_team_name = models.ForeignKey(Team, on_delete=models.SET_NULL, default=None, null=True, related_name='%(class)s')
    emp_hourly_rate = models.FloatField(default=15)
    emp_work_arrangement = models.ManyToManyField(WorkArrangement)

    def __str__(self):
        return self.emp_name

    class Meta:
        abstract = True


class TeamEmployee(Employee):
    additional_pay_percentage = 0
    def __str__(self):
        return self.emp_name


class TeamLeader(Employee):
    additional_pay_percentage = 10
    #emp_name = models.ForeignKey(TeamEmployee, on_delete=models.CASCADE)
    emp_team_name = models.OneToOneField(Team, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.emp_name)

    def __del__(self):
        pass
    #destructor
    #add team lead to TeamEmployee






