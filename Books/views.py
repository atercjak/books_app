from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from tablib import Dataset
from .models import Book
from . import forms
from django.views.generic import ListView


def upload_library(request):
    if request.method == 'POST':
        dataset = Dataset()
        new_books = request.FILES['my_file']
        imported_data = dataset.load(new_books.read(), format='xlsx')
        for data in imported_data:
            value = Book(
                data[0],
                data[1],
                data[2]
            )
            value.save()

    else:
        return render(request, 'Books/make-library.html')

    return redirect(reverse_lazy('Home:home'))


def add_book(request):
    form = forms.BookAddForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        else:
            return render(request, 'Books/add-book.html', {'form': form})
        return redirect(reverse_lazy('Home:home'))
    return render(request, 'Books/add-book.html', {'form': form})


class ViewAllBooks(ListView):
    model = Book
    template_name = 'Books/book-list.html'
    context_object_name = 'books'
