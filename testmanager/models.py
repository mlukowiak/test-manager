from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class ScenarioType(models.Model):
    scenarioTypeName = models.CharField(max_length=256)

    def __str__(self):
        return self.scenarioTypeName

class ScenarioArea(models.Model):
    scenarioAreaName = models.CharField(max_length=256)

    def __str__(self):
        return self.scenarioAreaName

class Scenario(models.Model):
    scenarioTitle = models.CharField(max_length=256)
    scenarioArea = models.ForeignKey(ScenarioArea, on_delete=models.CASCADE)
    scenarioAuthor = models.ForeignKey(User, on_delete=models.CASCADE)
    scenarioDate = models.DateTimeField(default=timezone.now)
    scenarioDescription = models.TextField()
    scenarioType = models.ForeignKey(ScenarioType, on_delete=models.CASCADE)
    scenarioInitial = models.TextField(null=True, blank=True)
    scenarioFinal = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.scenarioTitle

    def get_absolute_url(self):
        return reverse('scenario-detail', kwargs={'pk': self.pk})

class Status(models.Model):
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.status

class TestCase(models.Model):
    testName = models.CharField(max_length=256)
    testCondition = models.TextField(null=True, blank=True)
    testSteps = models.TextField(null=True, blank=True)
    testExpectedResult = models.TextField(null=True, blank=True)
    testStatus = models.ForeignKey(Status, on_delete=models.CASCADE)
    testScenario = models.ForeignKey(Scenario, on_delete=models.CASCADE)
    testAuthor = models.ForeignKey(User, on_delete=models.CASCADE)
    testDate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.testName

class Comment(models.Model):
    commentText = models.CharField(max_length=256)
    commentScenario = models.ForeignKey(Scenario, on_delete=models.CASCADE)
    commentAuthor = models.ForeignKey(User, on_delete=models.CASCADE)
    commentDate = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('scenario-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.commentText

