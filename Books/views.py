from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from tablib import Dataset
from .models import Book


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
