from django.urls import path
from .views import ScenarioListView, ScenarioDetailView, ScenarioCreateView, ScenarioDeleteView, CommentCreateView, MyScenarioListView, AllScenarioListView, SearchResultsView

urlpatterns = [
    path('', ScenarioListView.as_view(), name='home'),
    path('scenario/<int:pk>/', ScenarioDetailView.as_view(), name='scenario-detail'),
    path('scenario/<int:pk>/delete/', ScenarioDeleteView.as_view(), name='scenario-delete'),
    path('scenario/new/', ScenarioCreateView.as_view(), name='scenario-create'),
    path('comment/<int:scenario_id>/', CommentCreateView.as_view(), name='comment-create'),
    path('myscenarios/', MyScenarioListView.as_view(), name='myscenarios'),
    path('scenarios/', AllScenarioListView.as_view(), name='scenarios'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
]