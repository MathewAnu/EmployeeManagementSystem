from django.contrib import admin
from .models import *

admin.site.register(Team)
admin.site.register(TeamLeader)
admin.site.register(TeamEmployee)
admin.site.register(WorkArrangement)