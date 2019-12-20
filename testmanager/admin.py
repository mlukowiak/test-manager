from django.contrib import admin
from .models import ScenarioArea, ScenarioType, Scenario, Comment, Status, TestCase

admin.site.register(ScenarioArea)
admin.site.register(ScenarioType)
admin.site.register(Scenario)
admin.site.register(Comment)
admin.site.register(Status)
admin.site.register(TestCase)