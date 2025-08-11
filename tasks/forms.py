from django import forms
from tasks.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "priority", "due_date", "completed"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "priority": forms.Select(attrs={"class": "form-control"}),
            "due_date": forms.DateInput(
                attrs={"type": "date", "class": "form-control"}
            ),
            "completed": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
