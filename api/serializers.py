from testmanager.models import ScenarioType, ScenarioArea, Scenario, TestCase
from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')

class ScenarioTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ScenarioType
        fields = ('scenarioTypeName')
        
class ScenarioAreaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ScenarioArea
        fields = ('scenarioAreaName')

class ScenarioSerializer(serializers.HyperlinkedModelSerializer):
    scenarioAuthor = UserSerializer
    scenarioType = ScenarioTypeSerializer
    scenarioArea  = ScenarioAreaSerializer
    class Meta:
        model = Scenario
        fields = (
            'id', 
            'scenarioTitle',
            'scenarioAuthor',
            'scenarioType',
            'scenarioArea',
            'scenarioDate',
            'scenarioDescription',
            'scenarioInitial',
            'scenarioFinal',
            )

class TestCaseSerializer(serializers.HyperlinkedModelSerializer):
    testScenario = ScenarioSerializer
    testAuthor = UserSerializer
    class Meta:
        model = TestCase
        fields = (
            'id',
            'testScenario', 
            'testName',
            'testAuthor',
            'testCondition',
            'testSteps',
            'testExpectedResult',
            'testDate'
            )
    
