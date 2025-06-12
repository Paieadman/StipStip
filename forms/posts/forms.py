from django import forms

from .models import Question


# from . import models

class CreateQuestion(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']

