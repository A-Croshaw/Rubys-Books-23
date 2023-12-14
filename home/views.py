from django.shortcuts import get_object_or_404, render
from books.models import Book

def index(request):
    """ A view to return the home page """
    book = Book.objects.all()

    context = {
        "book": book,
    }

    return render(request, 'home/index.html', context,)
