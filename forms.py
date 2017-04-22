from django.forms import ModelForm,forms
from .models import Question
class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']