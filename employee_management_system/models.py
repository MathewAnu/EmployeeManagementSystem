from django.db import models


class Team(models.Model):
    team_name = models.CharField(max_length=20, primary_key=True)
    team_leader = models.CharField(max_length=20, blank=True, default=None)
    