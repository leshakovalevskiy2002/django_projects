from django.shortcuts import render
from django.http import HttpResponse
from .forms import AddBookForm
from .models import Catalog


def home(request):
    if request.method == 'POST':
        add_book_form = AddBookForm(data=request.POST)
        if add_book_form.is_valid():
            add_book_form.save()
    books = Catalog.objects.all()
    add_book_form = AddBookForm()

    return render(request, 'home.html', {
        "add_book_form": add_book_form,
        "books": books
    })