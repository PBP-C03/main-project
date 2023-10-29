from django import forms
from django.forms import ModelForm
from reviewbook.models import Review

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ["rating", "review"]

    rating = forms.IntegerField(label=False, widget=forms.NumberInput(attrs={'class': 'form-control', 'name': 'rating', 'required': 'required', 'id': 'rating', 'min': 0, 'max': 5}))
    review = forms.CharField(label=False, widget=forms.Textarea(attrs={'class': 'form-control', 'name': 'review', 'required': 'required', 'id': 'review'}))

class EditReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ["rating", "review"]

    rating = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'name': 'edit-rating', 'id': 'edit-rating', 'required': 'required', 'min': 0, 'max': 5}))
    review = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'name': 'edit-review', 'id': 'edit-review', 'required': 'required'}))