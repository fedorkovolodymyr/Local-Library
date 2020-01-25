from django.shortcuts import render

from .models import Author, Book, BookInstance, Genra

def index(request):
    """View funcrion for home page of site"""

    # Generate count of same of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__iexact='a').count()

    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with date context variable
    return render(request, 'index.html', context=context)