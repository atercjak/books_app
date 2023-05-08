from django import forms
from .models import Book


class LibraryForm(forms.Form):

    class Meta:
        model = Book
        fields = '__all__'


