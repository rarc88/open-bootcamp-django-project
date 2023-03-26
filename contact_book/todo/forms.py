from django import forms

from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        exclude = ['date',]
        widgets = {
            'estimated_end': forms.DateInput(attrs={'type': 'date'})
        }
