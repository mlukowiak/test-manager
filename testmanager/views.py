from .models import Scenario, Comment, TestCase, User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from datetime import datetime
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.db.models import Q

class ScenarioListView(LoginRequiredMixin, ListView):
    model = Scenario
    template_name = 'testmanager/home.html'
    latest_scenario_list = Scenario.objects.latest('id')
    context_object_name = 'latest_scenario_list'
    ordering = ['-scenarioDate']
    paginate_by = 5

class MyScenarioListView(LoginRequiredMixin, ListView):
    model = Scenario
    template_name = 'testmanager/myscenarios.html'
    context_object_name = 'myscenarios'

    def get_queryset(self):
        return Scenario.objects.filter(scenarioAuthor=self.request.user).order_by('-scenarioDate')

class AllScenarioListView(LoginRequiredMixin, ListView):
    model = Scenario
    template_name = 'testmanager/scenarios.html'
    scenario_list = Scenario.objects.all()
    context_object_name = 'scenario_list'
    ordering = ['-scenarioDate']

class SearchResultsView(ListView):
    model = Scenario
    template_name = 'scenarios.html'
    
    def get_queryset(self): 
        query = self.request.GET.get('q')
        object_list = Scenario.objects.filter(
            Q(scenarioTitle__icontains=query) | Q(scenarioDescription__icontains=query)
        )
        return object_list

class ScenarioDetailView(LoginRequiredMixin, DetailView):
    model = Scenario

class ScenarioCreateView(LoginRequiredMixin, CreateView):
    model = Scenario
    fields = [
        'scenarioTitle',
        'scenarioArea',
        'scenarioDescription',
        'scenarioType',
        'scenarioInitial',
        'scenarioFinal']

    def form_valid(self, form):
        form.instance.scenarioAuthor = self.request.user
        form.instance.scenarioDate = datetime.now()
        return super().form_valid(form)

class TestCaseCreateView(LoginRequiredMixin, CreateView):
    model = TestCase
    fields = [
        'commentText'
    ]

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = [
        'commentText'
    ]

    def form_valid(self, form):
        form.instance.commentAuthor = self.request.user
        form.instance.commentDate = datetime.now()
        form.instance.commentScenario = Scenario.objects.get(pk=self.kwargs.get('scenario_id'))
        return super().form_valid(form)

class ScenarioDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Scenario
    success_url = reverse_lazy('home')

    def test_func(self):
        scenario = self.get_object()
        if self.request.user == scenario.scenarioAuthor:
            return True
        return False