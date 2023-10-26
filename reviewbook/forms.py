from django.forms import ModelForm
from reviewbook.models import Review

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ["rating", "review"]