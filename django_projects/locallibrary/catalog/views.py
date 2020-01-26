from django.shortcuts import render
from django.views import generic

from .models import Author, Book, BookInstance, Genra

def index(request):
    """View funcrion for home page of site"""

    # Generate count of same of the main objects
    num_books = Book.objects.count()
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


class BookListView(generic.ListView):
    model = Book
    paginate_by = 3

    # def get_queryset(self):
    #     # return Book.objects.all()[:5]
    #     return Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
    
    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get the context
    #     context = super(BookListView, self).get_context_data(**kwargs)
    #     # Create any data and add it to the context
    #     context['some_data'] = 'This is just some data'
    #     return context

    # def get_context_data(self, **kwargs):
    #     conntext = super(BookListView, self).get_context_data(**kwargs)
    #     conntext['some_data'] = 'This is just some data'
    #     return conntext


class BookDetailView(generic.DetailView):
    model = Book
    

class AuthorListView(generic.ListView):
    model = Author


class AutorDetailView(generic.DetailView):
    model = Author