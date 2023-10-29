from django.forms import ModelForm
from .models import Question, Comment

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ["title", "book", "content"]

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']