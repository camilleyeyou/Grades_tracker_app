from django import forms
from .models import Grade
from .models import Goal


class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['subject', 'grade']
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'grade': forms.TextInput(attrs={'class': 'form-control'}),
        }

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['subject', 'target_grade', 'deadline']
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'target_grade': forms.TextInput(attrs={'class': 'form-control'}),
            'deadline': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }