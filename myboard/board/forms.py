from dataclasses import fields
from django import forms

from .models import Answer, Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']


# AnsworForm - fields : content
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']