from django.forms import ModelForm, TextInput, NumberInput
from uploadbook.models import UploadBook

class BookForm(ModelForm):
    class Meta:
        model = UploadBook
        fields = ["isbn", "title", "author", "year", "publisher", "image", "price", "stocks"]
        widgets = {
            "isbn": TextInput(attrs={'class': 'your-css-class', 'size': 40}),
            "title": TextInput(attrs={'class': 'your-css-class', 'size': 40}),
            "author": TextInput(attrs={'class': 'your-css-class', 'size': 40}),
            "year": NumberInput(attrs={'class': 'your-css-class', 'size': 40}),
            "publisher": TextInput(attrs={'class': 'your-css-class', 'size': 40}),
            "image": TextInput(attrs={'class': 'your-css-class', 'size': 40}),
            "price": NumberInput(attrs={'class': 'your-css-class', 'size': 40}),
            "stocks": NumberInput(attrs={'class': 'your-css-class', 'size': 40}),
        }