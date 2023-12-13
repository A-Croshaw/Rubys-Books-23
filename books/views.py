from django.shortcuts import get_object_or_404, redirect, reverse, render
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required
from .models import Book, Category
from .forms import BookForm


def all_books(request):
    """
    A view to render all books with sorting and searching
    """
    books = Book.objects.all()
    categories = None
    query = None
    sort = None
    dir = None

    if request.GET:

        if 'sort' in request.GET:
            sorting = request.GET['sort']
            sort = sorting
            if sorting == 'title':
                sorting = 'lower_title'
                books = books.annotate(lower_title=Lower('title'))
            if sorting == 'category':
                sorting = 'category__name'
            if 'dir' in request.GET:
                dir = request.GET['dir']
                if dir == 'desc':
                    sorting = f'-{sorting}'
            books = books.order_by(sorting)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            books = books.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
    
        if 'q' in request.GET:
                query = request.GET['q']
                if not query:
                    messages.error(request, "No Books with that criteria")
                    return redirect(reverse('books'))
                
                queries = Q(title__icontains=query) | Q(description__icontains=query)
                books = books.filter(queries)

    sorted = f'{sort}_{dir}'
    context = {
        'books': books,
        'search_term': query,
        'sorted_categories': categories,
        'sorted': sorted,
    }

    return render(request, 'books/books.html', context)


def book_view(request, book_id):
    """ View to see full book """

    book = get_object_or_404(Book, pk=book_id)

    context = {
        'book': book,
    }

    return render(request, 'books/book_view.html', context)


@login_required
def book_management(request):
    """
    A view for book management for admin users
    """
    books = Book.objects.all()
    query = None

    if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "No Books with that criteria")
            
            queries = Q(title__icontains=query) | Q(description__icontains=query)
            books = books.filter(queries)

    context = {
        'books': books,
        'search_term': query,
    }

    return render(request, 'books/book-management.html', context)


@login_required
def add_book(request):
    """ Adding books to the store admin users only """
    if not request.user.is_superuser:
        messages.error(request, 'Admin users only.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save()
            messages.success(request, 'The Book was successfully added')
            return redirect(reverse('book_view', args=[book.id]))
        else:
            messages.error(request, 'failed to add the book. Please ensure the details are correct and all fields that are required are entered.')
    else:
        form = BookForm()
        
    template = 'books/add_book.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_book(request, book_id):
    """ Edit a book in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Admin users only.')
        return redirect(reverse('home'))

    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'book was successfully updated!')
            return redirect(reverse('book_view', args=[book.id]))
        else:
            messages.error(request, 'Updating book failed. Please ensure the details are valid.')
    else:
        form = BookForm(instance=book)
        messages.info(request, f'Editing of {book.title}')

    template = 'books/edit_book.html'
    context = {
        'form': form,
        'book': book,
    }

    return render(request, template, context)


@login_required
def book_delete(request, book_id):
    """ Delete Book from Store """
    if not request.user.is_superuser:
        messages.error(request, 'Admin users only.')
        return redirect(reverse('home'))

    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    messages.success(request, 'Book has been delete successfully!')
    return redirect(reverse('books'))
