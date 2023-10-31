from django.forms import ModelForm
from uploadbook.models import UploadBook

class BookForm(ModelForm):
    class Meta:
        model = UploadBook
        fields = ["isbn", "title", "author", "year", "publisher", "image", "price", "stocks"]