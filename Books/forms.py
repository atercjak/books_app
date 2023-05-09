from django import forms
from .models import Book, Category


class LibraryForm(forms.Form):

    class Meta:
        model = Book
        fields = '__all__'


class BookAddForm(forms.Form):
    author = forms.CharField(label='Autor')
    title = forms.CharField(label='Tytuł')
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Kategoria')

    class Meta:
        model = Book
        fields = ('author', 'title', 'category')

    def save(self, commit=True):
        book = Book.objects.create(
            author=self.cleaned_data.get('author'),
            title=self.cleaned_data.get('title')
        )

        if commit:
            book.save()

        return book

