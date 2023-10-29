from django.forms import ModelForm
from cartbook.models import Book_Cart

class NoteForm(ModelForm):
    class Meta:
        model = Book_Cart
        fields = ["notes"]

