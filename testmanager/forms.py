from .models import Scenario, ScenarioArea, ScenarioType, Comment
from django import forms

class newScenario(forms.ModelForm):
    scenarioTitle = forms.CharField(label="", help_text="", widget=forms.TextInput(attrs={'placeholder': 'Tytuł'}))
    scenarioArea = forms.ModelChoiceField(label="", queryset=ScenarioArea.objects.all(), empty_label="Wybierz projekt")
    scenarioType = forms.ModelChoiceField(label="", queryset=ScenarioType.objects.all(), empty_label="Wybierz typ testów")
    scenarioDescription = forms.CharField(label="", help_text="", widget=forms.Textarea(attrs={'placeholder': 'Opis', 'class': 'materialize-textarea'}))
    scenarioInitial = forms.CharField(required=False, label="", help_text="", widget=forms.Textarea(attrs={'placeholder': 'Czynności przygotowawcze', 'class': 'materialize-textarea'}))
    scenarioFinal = forms.CharField(required=False, label="", help_text="", widget=forms.Textarea(attrs={'placeholder': 'Czynności końcowe', 'class': 'materialize-textarea'}))
    
    class Meta:
        model = Scenario
        fields = [
            'scenarioTitle',
            'scenarioArea',
            'scenarioDescription',
            'scenarioType',
            'scenarioInitial',
            'scenarioFinal'
            ]

class newComment(forms.ModelForm):
    commentText = forms.CharField(required=False, label="", help_text="", widget=forms.Textarea(attrs={'placeholder': 'Treść Twojego komentarza', 'class': 'materialize-textarea'}))

    class Meta:
        model = Comment
        fields = [
        'commentText',
        # 'commentScenario'
    ]