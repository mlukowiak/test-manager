from django.shortcuts import render
from rest_framework import viewsets
from testmanager.models import Scenario, TestCase, ScenarioType, ScenarioArea
from django.contrib.auth.models import User
from .serializers import ScenarioSerializer, TestCaseSerializer, UserSerializer, ScenarioAreaSerializer, ScenarioTypeSerializer

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ScenarioTypeView(viewsets.ModelViewSet):
    queryset = ScenarioType.objects.all()
    serializer_class = ScenarioTypeSerializer

class ScenarioAreaView(viewsets.ModelViewSet):
    queryset = ScenarioArea.objects.all()
    serializer_class = ScenarioAreaSerializer

class ScenarioView(viewsets.ModelViewSet):
    queryset = Scenario.objects.all()
    serializer_class = ScenarioSerializer

class TestCaseView(viewsets.ModelViewSet):
    queryset = TestCase.objects.all()
    serializer_class = TestCaseSerializer
